import json
import os
from datetime import datetime
from .logger import logger

class PostStorage:
    def __init__(self, output_file):
        self.output_file = output_file
        self._ensure_directory_exists()

    def _ensure_directory_exists(self):
        """Ensure the output directory exists."""
        os.makedirs(os.path.dirname(self.output_file), exist_ok=True)

    def save_generated_posts(self, posts):
        try:
            output = {
                "generated_at": datetime.now().isoformat(),
                "posts": posts
            }
            
            with open(self.output_file, 'w', encoding='utf-8') as f:
                json.dump(output, f, indent=4)
            logger.info(f"Successfully saved {len(posts)} posts to {self.output_file}")
        except Exception as e:
            logger.error(f"Failed to save posts: {e}")
            raise
