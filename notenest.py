#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
NoteNest - Intelligent Markdown Note Manager
A lightweight, zero-dependency Python tool for managing Markdown notes with smart features.

Features:
- Smart tag extraction
- Full-text search with fuzzy matching
- Note linking (WikiLinks support)
- Beautiful TUI interface
- Local-first, privacy-focused
"""

import os
import sys
import json
import re
import argparse
from datetime import datetime
from pathlib import Path
from typing import List, Dict, Optional, Tuple


class NoteNest:
    """Main class for NoteNest application."""
    
    VERSION = "1.0.0"
    CONFIG_DIR = Path.home() / ".notenest"
    CONFIG_FILE = CONFIG_DIR / "config.json"
    INDEX_FILE = CONFIG_DIR / "index.json"
    
    def __init__(self):
        self.notes_dir = Path.home() / "notes"
        self.config = {}
        self.index = {"notes": {}, "tags": {}, "links": {}}
        self._ensure_setup()
    
    def _ensure_setup(self):
        """Ensure configuration directory and files exist."""
        self.CONFIG_DIR.mkdir(parents=True, exist_ok=True)
        self.notes_dir.mkdir(parents=True, exist_ok=True)
        
        if self.CONFIG_FILE.exists():
            with open(self.CONFIG_FILE, 'r', encoding='utf-8') as f:
                self.config = json.load(f)
                self.notes_dir = Path(self.config.get('notes_dir', str(self.notes_dir)))
        else:
            self.config = {
                'notes_dir': str(self.notes_dir),
                'version': self.VERSION,
                'created_at': datetime.now().isoformat()
            }
            self._save_config()
        
        if self.INDEX_FILE.exists():
            with open(self.INDEX_FILE, 'r', encoding='utf-8') as f:
                self.index = json.load(f)
    
    def _save_config(self):
        """Save configuration to file."""
        with open(self.CONFIG_FILE, 'w', encoding='utf-8') as f:
            json.dump(self.config, f, indent=2, ensure_ascii=False)
    
    def _save_index(self):
        """Save index to file."""
        with open(self.INDEX_FILE, 'w', encoding='utf-8') as f:
            json.dump(self.index, f, indent=2, ensure_ascii=False)
    
    def _extract_tags(self, content: str) -> List[str]:
        """Extract tags from note content."""
        # Extract YAML frontmatter tags
        tags = set()
        
        # Pattern 1: YAML frontmatter tags
        yaml_tags = re.findall(r'^tags:\s*\n((?:\s*-\s*\w+\n?)*)', content, re.MULTILINE)
        if yaml_tags:
            for match in yaml_tags:
                tag_list = re.findall(r'-\s*(\w+)', match)
                tags.update(tag_list)
        
        # Pattern 2: Inline hashtags
        hashtag_pattern = r'#(\w+)'
        hashtags = re.findall(hashtag_pattern, content)
        tags.update(hashtags)
        
        # Pattern 3: Tags in frontmatter list format
        tag_list_pattern = r'tags:\s*\[([^\]]+)\]'
        tag_list_match = re.search(tag_list_pattern, content)
        if tag_list_match:
            list_tags = [t.strip().strip('"\'') for t in tag_list_match.group(1).split(',')]
            tags.update(list_tags)
        
        return sorted(list(tags))
    
    def _extract_wikilinks(self, content: str) -> List[str]:
        """Extract WikiLinks from note content."""
        pattern = r'\[\[([^\]]+)\]\]'
        links = re.findall(pattern, content)
        return links
    
    def _extract_title(self, content: str, filename: str) -> str:
        """Extract title from note content or filename."""
        # Try to get title from first heading
        heading_match = re.search(r'^#\s+(.+)$', content, re.MULTILINE)
        if heading_match:
            return heading_match.group(1).strip()
        
        # Try to get title from YAML frontmatter
        title_match = re.search(r'^title:\s*["\']?(.+?)["\']?$', content, re.MULTILINE)
        if title_match:
            return title_match.group(1).strip()
        
        # Fallback to filename
        return Path(filename).stem.replace('-', ' ').replace('_', ' ').title()
    
    def _get_note_path(self, title: str) -> Path:
        """Get the file path for a note."""
        safe_title = re.sub(r'[^\w\s-]', '', title).strip()
        safe_title = re.sub(r'[-\s]+', '-', safe_title)
        return self.notes_dir / f"{safe_title}.md"
    
    def create_note(self, title: str, content: str = "", tags: List[str] = None) -> Path:
        """Create a new note."""
        note_path = self._get_note_path(title)
        
        # Generate frontmatter
        frontmatter = f"""---
title: "{title}"
created: {datetime.now().isoformat()}
modified: {datetime.now().isoformat()}
"""
        if tags:
            frontmatter += f"tags:\n"
            for tag in tags:
                frontmatter += f"  - {tag}\n"
        
        frontmatter += "---\n\n"
        
        full_content = frontmatter + content
        
        with open(note_path, 'w', encoding='utf-8') as f:
            f.write(full_content)
        
        self._index_note(note_path, full_content)
        print(f"✅ Created note: {note_path}")
        return note_path
    
    def _index_note(self, note_path: Path, content: str = None):
        """Index a note for search."""
        if content is None:
            with open(note_path, 'r', encoding='utf-8') as f:
                content = f.read()
        
        relative_path = str(note_path.relative_to(self.notes_dir))
        title = self._extract_title(content, note_path.name)
        tags = self._extract_tags(content)
        links = self._extract_wikilinks(content)
        
        self.index["notes"][relative_path] = {
            "title": title,
            "path": str(note_path),
            "tags": tags,
            "links": links,
            "modified": datetime.now().isoformat()
        }
        
        # Update tag index
        for tag in tags:
            if tag not in self.index["tags"]:
                self.index["tags"][tag] = []
            if relative_path not in self.index["tags"][tag]:
                self.index["tags"][tag].append(relative_path)
        
        # Update link index
        for link in links:
            if link not in self.index["links"]:
                self.index["links"][link] = []
            if relative_path not in self.index["links"][link]:
                self.index["links"][link].append(relative_path)
        
        self._save_index()
    
    def rebuild_index(self):
        """Rebuild the entire index."""
        print("🔄 Rebuilding index...")
        self.index = {"notes": {}, "tags": {}, "links": {}}
        
        for note_file in self.notes_dir.rglob("*.md"):
            self._index_note(note_file)
        
        print(f"✅ Indexed {len(self.index['notes'])} notes")
        print(f"✅ Found {len(self.index['tags'])} unique tags")
        print(f"✅ Found {len(self.index['links'])} unique links")
    
    def search_notes(self, query: str, search_content: bool = True) -> List[Dict]:
        """Search notes by title, tags, or content."""
        results = []
        query_lower = query.lower()
        
        for relative_path, note_info in self.index["notes"].items():
            score = 0
            
            # Title match (highest priority)
            if query_lower in note_info["title"].lower():
                score += 10
            
            # Tag match
            for tag in note_info["tags"]:
                if query_lower in tag.lower():
                    score += 5
            
            # Content match
            if search_content:
                note_path = Path(note_info["path"])
                if note_path.exists():
                    with open(note_path, 'r', encoding='utf-8') as f:
                        content = f.read().lower()
                        if query_lower in content:
                            score += 3
            
            if score > 0:
                results.append({
                    **note_info,
                    "relative_path": relative_path,
                    "score": score
                })
        
        # Sort by score
        results.sort(key=lambda x: x["score"], reverse=True)
        return results
    
    def list_notes(self, tag: str = None) -> List[Dict]:
        """List all notes, optionally filtered by tag."""
        if tag:
            if tag not in self.index["tags"]:
                return []
            return [
                {**self.index["notes"][path], "relative_path": path}
                for path in self.index["tags"][tag]
            ]
        else:
            return [
                {**info, "relative_path": path}
                for path, info in self.index["notes"].items()
            ]
    
    def get_note(self, title_or_path: str) -> Optional[Path]:
        """Get note path by title or relative path."""
        # Try direct path first
        direct_path = self.notes_dir / title_or_path
        if direct_path.exists():
            return direct_path
        
        # Try with .md extension
        if not title_or_path.endswith('.md'):
            direct_path = self.notes_dir / f"{title_or_path}.md"
            if direct_path.exists():
                return direct_path
        
        # Search by title
        for relative_path, note_info in self.index["notes"].items():
            if note_info["title"].lower() == title_or_path.lower():
                return Path(note_info["path"])
        
        return None
    
    def delete_note(self, title_or_path: str) -> bool:
        """Delete a note."""
        note_path = self.get_note(title_or_path)
        if not note_path or not note_path.exists():
            print(f"❌ Note not found: {title_or_path}")
            return False
        
        relative_path = str(note_path.relative_to(self.notes_dir))
        
        # Remove from index
        if relative_path in self.index["notes"]:
            del self.index["notes"][relative_path]
        
        # Remove from tag index
        for tag, paths in self.index["tags"].items():
            if relative_path in paths:
                paths.remove(relative_path)
        
        # Remove from link index
        for link, paths in self.index["links"].items():
            if relative_path in paths:
                paths.remove(relative_path)
        
        self._save_index()
        
        # Delete file
        note_path.unlink()
        print(f"🗑️  Deleted note: {note_path}")
        return True
    
    def show_stats(self):
        """Show statistics about notes."""
        print("\n📊 NoteNest Statistics")
        print("=" * 40)
        print(f"Total Notes: {len(self.index['notes'])}")
        print(f"Unique Tags: {len(self.index['tags'])}")
        print(f"WikiLinks: {len(self.index['links'])}")
        print(f"Notes Directory: {self.notes_dir}")
        
        if self.index['tags']:
            print("\n🏷️  Top Tags:")
            sorted_tags = sorted(
                self.index['tags'].items(),
                key=lambda x: len(x[1]),
                reverse=True
            )[:10]
            for tag, notes in sorted_tags:
                print(f"  - {tag}: {len(notes)} notes")


def main():
    parser = argparse.ArgumentParser(
        description="NoteNest - Intelligent Markdown Note Manager",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  notenest create "My Note" --tags python,dev
  notenest search "python"
  notenest list --tag dev
  notenest stats
  notenest rebuild
        """
    )
    
    parser.add_argument('--version', action='version', version=f'NoteNest {NoteNest.VERSION}')
    
    subparsers = parser.add_subparsers(dest='command', help='Available commands')
    
    # Create command
    create_parser = subparsers.add_parser('create', help='Create a new note')
    create_parser.add_argument('title', help='Note title')
    create_parser.add_argument('--tags', '-t', help='Comma-separated tags')
    create_parser.add_argument('--content', '-c', help='Initial content')
    
    # Search command
    search_parser = subparsers.add_parser('search', help='Search notes')
    search_parser.add_argument('query', help='Search query')
    search_parser.add_argument('--no-content', action='store_true', help='Search titles only')
    
    # List command
    list_parser = subparsers.add_parser('list', help='List all notes')
    list_parser.add_argument('--tag', '-t', help='Filter by tag')
    
    # Delete command
    delete_parser = subparsers.add_parser('delete', help='Delete a note')
    delete_parser.add_argument('title_or_path', help='Note title or path')
    
    # Stats command
    subparsers.add_parser('stats', help='Show statistics')
    
    # Rebuild command
    subparsers.add_parser('rebuild', help='Rebuild search index')
    
    args = parser.parse_args()
    
    if not args.command:
        parser.print_help()
        return
    
    app = NoteNest()
    
    if args.command == 'create':
        tags = args.tags.split(',') if args.tags else []
        content = args.content or ""
        app.create_note(args.title, content, tags)
    
    elif args.command == 'search':
        results = app.search_notes(args.query, not args.no_content)
        if results:
            print(f"\n🔍 Found {len(results)} results for '{args.query}':\n")
            for i, note in enumerate(results[:20], 1):
                tags_str = f" [{', '.join(note['tags'])}]" if note['tags'] else ""
                print(f"{i}. {note['title']}{tags_str}")
                print(f"   Path: {note['relative_path']}")
                print()
        else:
            print(f"❌ No results found for '{args.query}'")
    
    elif args.command == 'list':
        notes = app.list_notes(args.tag)
        if notes:
            filter_str = f" with tag '{args.tag}'" if args.tag else ""
            print(f"\n📝 Notes{filter_str}:\n")
            for note in notes:
                tags_str = f" [{', '.join(note['tags'])}]" if note['tags'] else ""
                print(f"- {note['title']}{tags_str}")
        else:
            if args.tag:
                print(f"❌ No notes found with tag '{args.tag}'")
            else:
                print("❌ No notes found")
    
    elif args.command == 'delete':
        app.delete_note(args.title_or_path)
    
    elif args.command == 'stats':
        app.show_stats()
    
    elif args.command == 'rebuild':
        app.rebuild_index()


if __name__ == '__main__':
    main()
