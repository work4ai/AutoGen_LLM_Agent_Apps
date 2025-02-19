# AutoGen-Based Nested Chat with Reflection Mechanism

## Overview
This project demonstrates the use of AutoGen to implement a nested chat system with a reflection-based review mechanism. The system generates and refines a blog post through multiple agents, each with a specific role in the review process.

## Features
- **Multi-Agent Collaboration**: Uses different agents for writing, critiquing, and reviewing content.
- **Reflection-Based Review**: Each reviewer provides feedback, which is aggregated for final refinement.
- **Nested Chat Workflow**: Implements a structured review system where feedback is collected in stages.
- **SEO & Compliance Checks**: Ensures the content is optimized and adheres to legal and ethical guidelines.

## Installation & Setup
1. Install `autogen` package if not already installed:
   ```sh
   pip install autogen
   ```
2. Set up your Groq API key:
   ```python
   GROQ_API_KEY = "your_api_key_here"
   ```
3. Adjust the LLM configuration:
   ```python
   llm_config = {
       "model": "llama3-70b-8192",  # Adjust as needed
       "api_key": GROQ_API_KEY,
       "base_url": "https://api.groq.com/openai/v1"
   }
   ```

## Agents & Responsibilities
1. **Writer**: Creates a concise blog post based on the given topic.
2. **Critic**: Reviews the writing and provides constructive feedback.
3. **SEO Reviewer**: Ensures SEO optimization.
4. **Legal Reviewer**: Checks for legal compliance.
5. **Ethics Reviewer**: Validates ethical considerations.
6. **Meta Reviewer**: Aggregates feedback and gives final recommendations.

## Execution Flow
1. The `writer` generates the initial blog post.
2. The `critic` initiates a nested review process involving the SEO, legal, and ethics reviewers.
3. Feedback is aggregated by the `meta reviewer`.
4. The `critic` provides a final refined output.
5. The reviewed content is displayed as a summary.

## Running the Script
Execute the script with:
```sh
python script.py
```

## Expected Output
- A refined blog post optimized for engagement, compliance, and SEO.
- Summarized feedback from different reviewers.

## Customization
- Modify `task` to change the writing prompt.
- Adjust `llm_config` to use different models.
- Extend reviewers or change their evaluation criteria as needed.

## License
This project is licensed under the MIT License.

