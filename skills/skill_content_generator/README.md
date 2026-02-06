# Skill: Content Generator
Generates multimodal media based on a planner's task and character constraints.

- **Input Contract**:
```json
{
  "prompt": "string",
  "character_ref": "string",
  "format": "video|image|text"
}
```

- **Output Contract**:
```json
{
  "content_id": "string",
  "format": "video|image|text",
  "content_url": "string",
  "metadata": {
    "title": "string",
    "caption": "string"
  }
}
```