+++
kind  = "proof"
of    = "lemma-weil-pbc-h1-torsor-comparison"
+++
By [def-weil-pbc-finite-torsors] the two sides classify $M$-torsors, which by
[thm-galois-lc-etale] are the simply transitive $M$-actions on finite etale schemes surjective over
the base. The equivalence of
[thm-weil-pbc-finite-etale-lifting] preserves such actions and their
isomorphism classes, giving the bijection.

In detail: by [lemma-weil-pbc-finite-locally-constant-etale-equivalence], an
$\underline M$-torsor on $Y$ is a finite etale $Y$-scheme $P$, surjective
over $Y$, with a simply transitive $M$-action, and likewise on $Y_0$. By
[thm-weil-pbc-finite-etale-lifting] for the henselian pair $(A,I)$ and the
proper $Y\to\operatorname{Spec}A$, every finite etale $P_0\to Y_0$ is the
restriction of a finite etale $P\to Y$, unique up to unique isomorphism, and
every automorphism $m:P_0\to P_0$ and every multiplication diagram lift
uniquely. Uniqueness of lifted morphisms preserves the group law, and simple
transitivity, i.e. that $M\times P\to P\times_YP$ is an isomorphism, lifts
because this morphism is the unique lift of the corresponding isomorphism
over $Y_0$. Surjectivity lifts as well: the image of a finite etale $P\to Y$
is open and closed, and it contains $Y_0$ when $P_0\to Y_0$ is surjective;
open and closed subschemes are finite etale, so by the equivalence of
[thm-weil-pbc-finite-etale-lifting] an open and closed subscheme of $Y$
containing $Y_0$ is $Y$. Restriction and lifting are therefore inverse on isomorphism
classes, which is the displayed $H^1$ bijection.
