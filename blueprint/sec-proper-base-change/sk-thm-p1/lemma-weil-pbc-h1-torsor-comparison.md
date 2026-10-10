+++
id = "lemma-weil-pbc-h1-torsor-comparison"
kind = "lemma"
title = "Finite-etale torsor comparison"
order = 1139
uses = ["def-weil-pbc-finite-torsors", "def-weil-pbc-strict-henselian-setup", "lemma-weil-pbc-etale-degree-zero", "lemma-weil-pbc-finite-etale-henselian-lifting", "lemma-weil-pbc-finite-locally-constant-etale-equivalence", "thm-galois-lc-etale", "thm-weil-pbc-finite-etale-lifting"]
+++
Let $(A,I)$ be a henselian pair, let $Y\to\operatorname{Spec}A$ be proper,
and let $Y_0=Y\times_AA/I$. For every finite abelian group $M$, restriction
induces a bijection

$$
 H^1(Y,\underline M)\xrightarrow{\sim}H^1(Y_0,\underline M).
$$

## Proof

By [def-weil-pbc-finite-torsors] the two sides classify $M$-torsors, which by
[thm-galois-lc-etale] are the simply transitive $M$-actions on finite etale schemes. The equivalence of
[thm-weil-pbc-finite-etale-lifting] preserves such actions and their
isomorphism classes, giving the bijection.

In detail: by [lemma-weil-pbc-finite-locally-constant-etale-equivalence], an
$\underline M$-torsor on $Y$ is a finite etale $Y$-scheme $P$ with a simply
transitive $M$-action, and likewise on $Y_0$. By
[thm-weil-pbc-finite-etale-lifting] for the henselian pair $(A,I)$ and the
proper $Y\to\operatorname{Spec}A$, every finite etale $P_0\to Y_0$ is the
restriction of a finite etale $P\to Y$, unique up to unique isomorphism, and
every automorphism $m:P_0\to P_0$ and every multiplication diagram lift
uniquely. Uniqueness of lifted morphisms preserves the group law, and simple
transitivity, i.e. that $M\times P\to P\times_YP$ is an isomorphism, lifts
because this morphism is the unique lift of the corresponding isomorphism
over $Y_0$. Restriction and lifting are therefore inverse on isomorphism
classes, which is the displayed $H^1$ bijection.
