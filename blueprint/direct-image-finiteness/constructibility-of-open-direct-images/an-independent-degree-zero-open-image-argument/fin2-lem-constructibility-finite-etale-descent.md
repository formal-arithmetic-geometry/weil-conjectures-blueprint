+++
id = "fin2-lem-constructibility-finite-etale-descent"
kind = "lemma"
title = "Descent of constructibility along finite etale surjections"
order = 3218
uses = ["def-weil-pbc-constructible-complexes", "def-weil-pbc-direct-image", "def-weil-pbc-inverse-image", "def-weil-pbc-scheme-conventions", "lem-fin-finite-morphism", "lemma-weil-pbc-finite-direct-image-exact", "lemma-weil-pbc-finite-stalk-formula", "thm-constructible-serre"]
+++
Let $\sigma:S'\to S$ be a
finite etale surjective
morphism with $S'$ and $S$ of finite type over $k$, and let $G$ be a
$\Lambda$-sheaf on $S_{{\mathrm{et}}}$ (the inverse image and direct
image of [def-weil-pbc-inverse-image] and
[def-weil-pbc-direct-image]). If $\sigma^{-1}G$ is
constructible, then
so is $G$; and $\sigma^{-1}G=0$ implies $G=0$.

## Proof

The unit $G\to\sigma_*\sigma^{-1}G$ of the
def:weil-pbc-inverse-image-adjunction: at a geometric point
$\bar s$ of $S$ the target stalk is, by
[lemma-weil-pbc-finite-stalk-formula], the finite product of the
stalks $(\sigma^{-1}G)_{\bar s'}=G_{\bar s}$ over the geometric
points $\bar s'$ of the finite fibre $S'_{\bar s}$, and the unit is
the diagonal: injective, since $\sigma$ is surjective. The morphism
$\sigma$ is finite, so $\sigma_*$ is exact by
[lemma-weil-pbc-finite-direct-image-exact], and the constructible
$\sigma^{-1}G$ (constructible in the sense of
[def-weil-pbc-constructible-complexes]) pushes forward to the
constructible $\sigma_*\sigma^{-1}G$ by [lem-fin-finite-morphism]
(a finite morphism with constructible coefficients has constructible
direct image in the sense of [def-weil-pbc-direct-image], with
the stalks finite by
[lemma-weil-pbc-finite-stalk-formula]); the sheaf $G$ is the image
of the unit, hence a submodule of a constructible sheaf, so
constructible by the weak-Serre closure of
[thm-constructible-serre]. For the zero clause,
$\sigma^{-1}G=0$ gives $\sigma_*\sigma^{-1}G=0$, and the injection
$G\hookrightarrow\sigma_*\sigma^{-1}G$ gives $G=0$.
