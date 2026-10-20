# Collective predictive coding and System 3

[← Reading routes](../README.md) · [Paper map](06-paper-map.md) · [Next: time and memory →](04-time-memory-and-canalization.md)

**Source:** Taniguchi et al., arXiv:2503.06138v3, §§3.1–3.3, especially [PDF pp.17–20](https://arxiv.org/pdf/2503.06138v3#page=17). This module explains the authors' hypothesis and formalization; it does not claim experimental confirmation of the quad-process theory.

## What makes a collective system

System 3 concerns the organization that develops among agents, including the language, conventions, and institutions through which they coordinate. An individual can learn a word, but the community-level pattern is not stored wholly inside that individual. Across interactions, usage changes and constrains later participants. The paper treats this external symbolic organization as an adaptive process in its own right. [§3.1, PDF pp.16–17](https://arxiv.org/pdf/2503.06138v3#page=16)

CPC supplies a proposed mathematical perspective: agents encounter different parts of the world, form internal representations, and negotiate shared symbols. Symbol emergence is interpreted as approximate inference performed through distributed interactions. A language is thus more than a channel carrying already complete thoughts; in this account it is an evolving external representation of shared experience. The paper attributes the CPC hypothesis to Taniguchi (2024); Figure 4 is reused from that earlier work. [§3.2, Figure 4, PDF p.17](https://arxiv.org/pdf/2503.06138v3#page=17)

**Companion illustration:** two robots encounter objects from different viewpoints. Each learns local features. Through naming interactions, they may develop a shared distinction useful for their environment. The interesting collective change is not that both say the same token once; it is how token use and perceptual categories become coordinated. This is an explanatory example, not an experiment reported here.

## Variables and model direction

| Symbol | Role in the paper | Why it matters |
| --- | --- | --- |
| `k` | Index of an agent | Experience is distributed among participants. |
| `o^k` | Agent k's perceptual observations | These are grounded in sensorimotor interaction. |
| `z^k` | Agent k's internal representation | Agents need not share identical internal states. |
| `a^k` | Sequence of actions for agent k in the action-conditioned extension | Observations depend on what agents do. |
| `w` | Shared external symbolic representation, including language | The collective organization is a modeled variable. |
| `p` | Generative distribution | Specifies how symbols, representations, and observations are related in the model. |
| `q` | Approximate inference distribution | Describes the variational approximation rather than guaranteed access to an exact posterior. |

Source: [§3.2, PDF p.18](https://arxiv.org/pdf/2503.06138v3#page=18). The set notation collects agents; it does not imply a central observer actually has all their data.

Equations 1–2 introduce a simplified group model. On the generative side, a shared symbolic variable is associated with each agent's internal state, which in turn relates to its observations. On the inference side, each agent encodes its observations, and inter-agent interaction is associated with inference about the shared symbol. The factorization imposes modeling assumptions; it is not a description of every dependency in an actual society.

Equations 3–4 add actions and collect the agent-indexed variables into bold group variables. This brings CPC back to embodiment: the observations and actions arise from System 0 interactions and are processed by individual systems. The authors explicitly assume free-energy-related organization across the hierarchy. They do not make sensorimotor grounding unnecessary by introducing a social level. [Eqs.1–4, PDF p.18](https://arxiv.org/pdf/2503.06138v3#page=18), [clarification, PDF p.19](https://arxiv.org/pdf/2503.06138v3#page=19)

## Reading the objective by its jobs

Equations 5–6 express a collective objective using a KL divergence between the approximate joint distribution and the generative joint distribution, then expand it as an expected log ratio. Equation 7 separates log-ratio contributions. Equation 8 names three components:

| Component | Explanatory role | What it should not be confused with |
| --- | --- | --- |
| Collective regularization | Relates the inferred symbolic organization to its prior distribution | A direct numerical measure of social consensus, truth, or fairness |
| Individual prediction error | Penalizes poor prediction of each agent's observations given its representation and actions | The whole cost of coordinating a community |
| Individual regularization | Relates an agent's inferred representation to the representation distribution conditioned on symbols and actions | A requirement that every agent has the same private state |

This is a role-based paraphrase of [Eqs.5–8, PDF p.18](https://arxiv.org/pdf/2503.06138v3#page=18), not a new derivation. Predictive accuracy and regularization jointly matter. Simply minimizing messages exchanged, forcing agreement, or counting votes does not implement the stated objective.

The authors propose that individual changes and naming interactions can collectively improve this objective without a central controller. They cite Metropolis–Hastings naming games as a constructive route for distributed symbol formation. Those cited models motivate the hypothesis; the paper does not establish convergence for arbitrary societies, arbitrary communication protocols, or modern LLM teams. [§3.2, PDF p.19](https://arxiv.org/pdf/2503.06138v3#page=19)

## Notation and derivation cautions

The rendered official v3 PDF was inspected, not just extracted text. **Equation 4 visibly contains an incomplete `q(o |)` factor.** Equation 7 uses `q(o)`. Treat the incomplete bar as a source typesetting issue and consult the surrounding discussion; do not silently fill in a conditioning variable and attribute the result to the authors. [PDF p.18](https://arxiv.org/pdf/2503.06138v3#page=18)

**Companion mathematical caution:** several expectations and constants need care before implementing these equations. A KL between normalized joint distributions, as displayed in Equation 5, is not automatically identical to the usual fixed-observation negative ELBO under every convention. Equation 7 contains an observation-distribution entropy contribution through `log q(o)`; Equation 8 does not display that contribution. If `q(o)` is held fixed, its contribution can be constant for an optimization, but that assumption should be stated. Conditional KL terms involving `z` or `w` also require the appropriate outer averaging for a scalar objective. The printed shorthand does not specify every integration convention.

These are implementation-readiness questions about the displayed formalism, not evidence against the whole conceptual framework and not an asserted erratum from the authors. This companion preserves the model's explanatory roles and does not supply a silently corrected objective. A future implementation should write down normalized distributions, conditional-independence assumptions, optimized variables, and all expectations before claiming to reproduce CPC.

## Communication, learning, and semiotic plasticity

Section 3.3 distinguishes immediate use from longer-term change. For an individual model, the authors contrast inference with learning. For a collective symbolic system, they contrast communication with symbol emergence. Both can occur in an interacting group, but a transient exchange using a frozen vocabulary does not by itself demonstrate lasting adaptation of that vocabulary. [§3.3, PDF p.20](https://arxiv.org/pdf/2503.06138v3#page=20)

The paper uses **semiotic plasticity** for the adaptability of symbol systems. This differs in locus from neural plasticity in individuals, although the two interact: public conventions constrain individual learning, and individual utterances and experiences can reshape conventions. An emergent symbol system is therefore neither wholly imposed from above nor reducible to one participant's private model. [§1, PDF p.4](https://arxiv.org/pdf/2503.06138v3#page=4), [§3.2, PDF p.19](https://arxiv.org/pdf/2503.06138v3#page=19)

## Questions to carry forward

1. What would distinguish a change in `w` from better inference by a single agent about an unchanged `w`?
2. Which observations and actions make a naming task embodied, rather than merely a token agreement task?
3. What dependencies would real social interaction add beyond the simplified factorization?
4. Which empirical measures could separate useful shared distinctions from agreement on a mistaken convention?
5. What assumptions are needed for a decentralized update rule to improve a well-defined collective objective?

These are companion discussion prompts. For the paper's own predictions and broader limits, continue to [implications and limitations](05-implications-limitations-and-questions.md).
