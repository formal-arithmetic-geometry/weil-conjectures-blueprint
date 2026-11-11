+++
kind = "proof"
of = "proposition-milnor-sequence--3"
order = 91006
uses = ["definition-ind-etale-pro-etale-weakly--3", "definition-weak-contractibility--1", "corollary-evaluation-weakly-contractible-objects--5", "corollary-evaluation-weakly-contractible-objects--6", "proposition-milnor-sequence--1"]
+++
Suppose now that the transition maps of a tower of modules are
epimorphisms. We show that $1-T$ is an epimorphism; then
$R^1\varprojlim_nM_n=0$ and the derived limit is $\varprojlim_nM_n$. By
Corollary [corollary-evaluation-weakly-contractible-objects] it suffices to check surjectivity on sections
over every weakly contractible $W$, where the maps $t_n$ are surjective.
Given $(a_n)$, choose $m_0$ arbitrarily and then, recursively, $m_{n+1}$
with $t_n(m_{n+1})=m_n-a_n$. Then $(1-T)(m_n)_n=(a_n)_n$. See
[Stacks, [0947](https://stacks.math.columbia.edu/tag/0947)].

*Source:* the proof of Proposition [proposition-milnor-sequence].
