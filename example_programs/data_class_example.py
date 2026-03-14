from dataclasses import dataclass, asdict
import json
import time

@dataclass
class AgentTokenDetails:
    token_count: int
    token_limit: int
    tokens_used: int
    tokens_remaining: int

@dataclass
class AgentProfile:
    agent_name: str
    model_engine: str
    temperature: float
    max_retries: int = 3
    is_active: bool = True
    token_details: AgentTokenDetails = None


gpt4 = AgentProfile(
    agent_name="Agent Smith",
    model_engine="gpt-4",
    temperature=0.7,
    max_retries=5,
    is_active=True,
    token_details=AgentTokenDetails(
        token_count=1000,
        token_limit=4096,
        tokens_used=500,
        tokens_remaining=3596
    )
)

gemini = AgentProfile(
    agent_name="Agent Johnson",
    model_engine="gemini-2",
    temperature=0.5
)

print(gemini.agent_name)
print(gpt4.agent_name)
print(gpt4.token_details.token_count)

gpt4_dict = asdict(gpt4)
gemini_dict = asdict(gemini)

print("GPT-4 Agent Profile:")
print(gpt4_dict)
print("\nGemini Agent Profile:")
print(gemini_dict)