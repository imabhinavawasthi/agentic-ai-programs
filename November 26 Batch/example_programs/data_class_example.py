from dataclasses import dataclass, asdict

@dataclass
class AgentConfig:
    model: str
    max_tokens: int
    temperature: int
    user_id: str


agentConfig = AgentConfig(
    model="gemini",
    max_tokens=100,
    temperature=123,
    user_id="54365tf"
)

print(agentConfig)
print(type(agentConfig))
print(asdict(agentConfig))