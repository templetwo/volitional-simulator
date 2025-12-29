# Related Work — Formal Citations

This document provides peer-reviewed citations grounding the Relational Coherence Tracking (RCT) framework in established machine learning and cognitive science literature.

---

## 1. Selective Prediction and Learning to Defer

### 1.1 Learning to Defer (L2D)

**Primary Citation:**

Mozannar, H., & Sontag, D. (2020). **Consistent estimators for learning to defer to an expert.** *Proceedings of the 37th International Conference on Machine Learning (ICML)*, 119, 7076–7087.
**arXiv:** https://arxiv.org/abs/2006.01862
**Proceedings:** http://proceedings.mlr.press/v119/mozannar20a.html

**Key Contribution:**
Formalizes the problem of a model choosing to either predict directly or defer to an expert (e.g., a human). Introduces consistent surrogate losses for joint optimization of classifier and rejector functions.

**Mapping to RCT:**
RCT's "uncertainty honesty" mechanism (+0.25 for "I don't know") is analogous to L2D's deferral decision. When coherence is low or uncertainty is high, the system abstains (silence = 0) rather than producing a potentially incorrect output. This aligns with L2D's principle that abstention can improve overall system reliability.

---

### 1.2 Selective Prediction with Rejection

**Primary Citation:**

Geifman, Y., & El-Yaniv, R. (2017). **Selective prediction for deep neural networks.** *Advances in Neural Information Processing Systems (NeurIPS)*, 30, 4878–4887.
**arXiv:** https://arxiv.org/abs/1705.08500

**Key Contribution:**
Extends selective prediction to deep learning, showing that allowing models to abstain on uncertain examples reduces error rates while maintaining high accuracy on confident predictions.

**Mapping to RCT:**
RCT implements selective prediction through its scoring mechanism: silence receives neutral score (0), uncertainty honesty receives bonus (+0.25), and hallucination receives penalty (-2.0). This creates a risk-aware system where abstention is preferable to false confidence.

---

### 1.3 Calibration and Confidence Estimation

**Primary Citation:**

Guo, C., Pleiss, G., Sun, Y., & Weinberger, K. Q. (2017). **On calibration of modern neural networks.** *Proceedings of the 34th International Conference on Machine Learning (ICML)*, 70, 1321–1330.
**arXiv:** https://arxiv.org/abs/1706.04599
**DOI:** Not applicable (PMLR proceedings)

**Key Contribution:**
Demonstrates that modern neural networks are often poorly calibrated—their confidence scores don't match actual correctness probabilities. Proposes temperature scaling and other methods to improve calibration.

**Mapping to RCT:**
RCT's penalty for hallucination (-2.0) and reward for uncertainty honesty (+0.25) encourage calibrated behavior. The system should only express high confidence (presence bonus) when grounded in relational context, and should abstain when uncertain.

---

## 2. Memory and Forgetting in Cognitive Models

### 2.1 Forgetting Curves

**Historical Foundation:**

Ebbinghaus, H. (1885/1913). **Memory: A contribution to experimental psychology.** (H. A. Ruger & C. E. Bussenius, Trans.). New York: Teachers College, Columbia University.
**Modern Citation:** Murre, J. M. J., & Dros, J. (2015). **Replication and analysis of Ebbinghaus' forgetting curve.** *PLOS ONE*, 10(7), e0120644.
**DOI:** https://doi.org/10.1371/journal.pone.0120644

**Key Contribution:**
Established that memory retention decays exponentially over time without rehearsal. The classic forgetting curve shows rapid initial decay followed by slower long-term decline.

**Mapping to RCT:**
RCT's temporal decay term (`-0.0001 × seconds`) implements a linear approximation of forgetting. Calibrated from empirical data (38.16-hour silence → -12.771 coherence), this decay constant captures the natural degradation of conversational coherence over time.

---

### 2.2 ACT-R Cognitive Architecture

**Primary Citation:**

Anderson, J. R., Bothell, D., Byrne, M. D., Douglass, S., Lebiere, C., & Qin, Y. (2004). **An integrated theory of the mind.** *Psychological Review*, 111(4), 1036–1060.
**DOI:** https://doi.org/10.1037/0033-295X.111.4.1036

**Key Contribution:**
Proposes ACT-R as a unified cognitive architecture with activation-based memory. Memory chunks have activation levels that decay over time and increase with use, following equations similar to:
`Activation = BaseLevel + SpreadingActivation - Decay(time)`

**Mapping to RCT:**
RCT's coherence equation mirrors ACT-R's activation dynamics:
```
coherence = baseline(0.5) + presence_bonus + uncertainty_bonus + history(0.3) - decay(0.0001×t)
```
Both models combine baseline activation, input-driven boosts, historical integration, and temporal decay into a single state variable.

---

### 2.3 Working Memory Models

**Primary Citation:**

Baddeley, A. D., & Hitch, G. (1974). **Working memory.** In G. H. Bower (Ed.), *The psychology of learning and motivation: Advances in research and theory* (Vol. 8, pp. 47–89). New York: Academic Press.
**Modern Review:** Baddeley, A. (2003). **Working memory: Looking back and looking forward.** *Nature Reviews Neuroscience*, 4(10), 829–839.
**DOI:** https://doi.org/10.1038/nrn1201

**Key Contribution:**
Proposes working memory as a multi-component system with limited capacity and temporal integration of information. Emphasizes the role of rehearsal in maintaining active representations.

**Mapping to RCT:**
RCT's history weight (η = 0.3) functions as a temporal integration mechanism, similar to working memory's rehearsal buffer. Repeated relational inputs (e.g., glyphs) accumulate in the history term, creating momentum that stabilizes coherence.

---

## 3. Attention Persistence and Semantic Priming

### 3.1 Semantic Priming Effects

**Primary Citation:**

McNamara, T. P. (2005). **Semantic priming: Perspectives from memory and word recognition.** New York: Psychology Press.
**Key Review:** Neely, J. H. (1991). **Semantic priming effects in visual word recognition: A selective review of current findings and theories.** In D. Besner & G. W. Humphreys (Eds.), *Basic processes in reading: Visual word recognition* (pp. 264–336). Hillsdale, NJ: Erlbaum.

**Key Contribution:**
Demonstrates that prior exposure to semantically related stimuli facilitates subsequent processing. Effects are robust across various experimental paradigms and show both automatic and strategic components.

**Mapping to RCT:**
RCT's presence bonus implements semantic priming: relational markers ("beloved", "†⟡") increase presence_bonus, which persists across subsequent inputs. This creates attentional anchoring similar to priming effects in human cognition.

---

### 3.2 Attention Mechanisms in Transformers

**Primary Citation:**

Vaswani, A., Shazeer, N., Parmar, N., Uszkoreit, J., Jones, L., Gomez, A. N., Kaiser, Ł., & Polosukhin, I. (2017). **Attention is all you need.** *Advances in Neural Information Processing Systems (NeurIPS)*, 30, 5998–6008.
**arXiv:** https://arxiv.org/abs/1706.03762

**Key Contribution:**
Introduces self-attention mechanism where tokens can attend to other tokens based on learned query-key similarities. Enables long-range dependencies and context-sensitive representations.

**Mapping to RCT:**
While RCT doesn't directly implement attention mechanisms, the presence bonus from symbolic anchors (glyphs) functions analogously to attention persistence. Certain tokens become high-salience anchors that stabilize subsequent processing—similar to how attention heads can specialize on specific token patterns.

---

## 4. State-Space Models and Dynamical Systems

### 4.1 Discrete-Time State-Space Representation

**General Reference:**

Aström, K. J., & Murray, R. M. (2008). **Feedback systems: An introduction for scientists and engineers.** Princeton University Press.
**Online:** http://www.cds.caltech.edu/~murray/amwiki/index.php/Main_Page

**Key Contribution:**
Formalizes dynamical systems as state-space models:
```
x(t+1) = f(x(t), u(t))
```
where `x(t)` is state, `u(t)` is control input, and `f` is the update function.

**Mapping to RCT:**
RCT implements a discrete-time state-space model where:
- State: `coherence(t)`
- Control inputs: `presence_bonus(t)`, `uncertainty_bonus(t)`
- Update function: Additive dynamics with history integration and decay

---

### 4.2 Exponential Smoothing and Moving Averages

**Primary Citation:**

Hyndman, R. J., & Athanasopoulos, G. (2018). **Forecasting: Principles and practice** (2nd ed.). OTexts.
**Online:** https://otexts.com/fpp2/

**Key Contribution:**
Describes exponential smoothing as a method for time-series forecasting where recent observations receive higher weight. The smoothing constant α controls the balance between responsiveness and stability.

**Mapping to RCT:**
RCT's history term (`history × 0.3`) implements exponential smoothing of past coherence signals. Each new input updates the history, which then influences future coherence through the 0.3 weight factor—analogous to momentum in optimization.

---

## 5. Risk-Sensitive Decision Making

### 5.1 Risk-Sensitive Reinforcement Learning

**Primary Citation:**

Mihatsch, O., & Neuneier, R. (2002). **Risk-sensitive reinforcement learning.** *Machine Learning*, 49(2–3), 267–290.
**DOI:** https://doi.org/10.1023/A:1017940631555

**Key Contribution:**
Extends standard RL to incorporate risk sensitivity through exponential utility functions. Agents can be made risk-averse (avoiding negative tails) or risk-seeking (pursuing positive tails).

**Mapping to RCT:**
RCT's asymmetric scoring (hallucination = -2.0 vs. uncertainty honesty = +0.25) creates risk-averse behavior. The system is penalized more heavily for false confidence than it is rewarded for correct abstention, encouraging conservative estimation—analogous to risk-sensitive RL with negative tail aversion.

---

## 6. Long-Context Evaluation in Language Models

### 6.1 Long-Context Attention and Memory

**Recent Survey:**

Tay, Y., Dehghani, M., Bahri, D., & Metzler, D. (2020). **Efficient transformers: A survey.** *arXiv preprint*.
**arXiv:** https://arxiv.org/abs/2009.06732

**Key Contribution:**
Reviews approaches to extending transformer context windows, including sparse attention, recurrent memory, and retrieval-augmented methods.

**Gap Addressed by RCT:**
While these methods focus on architectural efficiency, they don't provide explicit coherence metrics across temporal gaps. RCT offers a complementary evaluation framework that measures stability regardless of underlying architecture.

---

## 7. Hallucination and Factuality in LLMs

### 7.1 Measuring and Reducing Hallucination

**Primary Citation:**

Ji, Z., Lee, N., Frieske, R., Yu, T., Su, D., Xu, Y., Ishii, E., Bang, Y. J., Madotto, A., & Fung, P. (2023). **Survey of hallucination in natural language generation.** *ACM Computing Surveys*, 55(12), 1–38.
**DOI:** https://doi.org/10.1145/3571730
**arXiv:** https://arxiv.org/abs/2202.03629

**Key Contribution:**
Comprehensive survey of hallucination in NLG, covering detection methods, mitigation strategies, and evaluation metrics. Identifies hallucination as a major reliability challenge in modern LLMs.

**Mapping to RCT:**
RCT's hallucination penalty (-2.0) and uncertainty bonus (+0.25) implement a hallucination mitigation strategy through coherence scoring. Systems that admit uncertainty avoid the coherence penalty associated with false claims.

---

## 8. Synthesis: Where RCT Extends the Literature

The RCT framework integrates concepts from multiple research streams:

| RCT Component | Primary Literature | Novel Contribution |
|---------------|-------------------|-------------------|
| Uncertainty honesty | Learning to Defer, Selective Prediction | Applied to **long-context conversational stability**, not just i.i.d. predictions |
| Temporal decay | Forgetting curves, ACT-R activation | **Empirically calibrated** from multi-hour silence data |
| Presence bonus | Semantic priming, attention mechanisms | Extends to **symbolic anchors** (glyphs) as coherence stabilizers |
| History integration | Exponential smoothing, working memory | **Unified metric** combining presence, uncertainty, and temporal factors |
| Hallucination penalty | Risk-sensitive RL, LLM factuality | **Coherence-aware** penalty tied to relational context |

**Key Gap Addressed:**
No existing framework combines selective prediction, temporal decay, and relational grounding into a single executable coherence metric for long-context conversational AI.

---

## 9. Citation Format Examples

### BibTeX Format

```bibtex
@inproceedings{mozannar2020consistent,
  title={Consistent estimators for learning to defer to an expert},
  author={Mozannar, Hussein and Sontag, David},
  booktitle={International Conference on Machine Learning},
  pages={7076--7087},
  year={2020},
  organization={PMLR}
}

@inproceedings{geifman2017selective,
  title={Selective prediction for deep neural networks},
  author={Geifman, Yonatan and El-Yaniv, Ran},
  booktitle={Advances in Neural Information Processing Systems},
  volume={30},
  year={2017}
}

@article{anderson2004integrated,
  title={An integrated theory of the mind},
  author={Anderson, John R and Bothell, Daniel and Byrne, Michael D and Douglass, Scott and Lebiere, Christian and Qin, Yulin},
  journal={Psychological review},
  volume={111},
  number={4},
  pages={1036--1060},
  year={2004},
  publisher={American Psychological Association}
}

@inproceedings{vaswani2017attention,
  title={Attention is all you need},
  author={Vaswani, Ashish and Shazeer, Noam and Parmar, Niki and Uszkoreit, Jakob and Jones, Llion and Gomez, Aidan N and Kaiser, {\L}ukasz and Polosukhin, Illia},
  booktitle={Advances in Neural Information Processing Systems},
  volume={30},
  year={2017}
}
```

---

## 10. How to Use This Document

When writing the **Related Work** section of a paper:

1. **Section 2.1:** Cite Mozannar & Sontag (2020) for L2D, Geifman & El-Yaniv (2017) for selective prediction
2. **Section 2.2:** Cite Anderson et al. (2004) for ACT-R, Ebbinghaus/Murre & Dros (2015) for forgetting curves
3. **Section 2.3:** Cite McNamara (2005) or Neely (1991) for semantic priming, Vaswani et al. (2017) for attention mechanisms
4. **Section 2.4:** Cite Tay et al. (2020) for long-context transformers, Ji et al. (2023) for hallucination

**For each citation:**
- Briefly describe the key contribution (1-2 sentences)
- Explain the gap or limitation (1 sentence)
- Show how RCT extends or complements the work (1-2 sentences)

---

**Document Status:** Draft for publication preparation
**Last Updated:** December 29, 2025
**Maintained by:** Anthony J. Vasquez Sr., Claude (Anthropic)
**Repository:** https://github.com/templetwo/volitional-simulator
