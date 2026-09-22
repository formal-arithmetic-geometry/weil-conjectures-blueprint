+++
id = "lem-fin-finite-boundary-comparison"
kind = "lemma"
title = "A proper direct image detects a comparison off a finite boundary"
order = 5225
lean = ["AlgebraicGeometry.Etale.isIso_of_isIso_restrict_and_derivedPushforward"]
+++
Let $b:Y\to S$ be proper, let $a:G\hookrightarrow Y$ be open with closed
complement $i:Z\hookrightarrow Y$, and suppose $bi$ is finite. Let
$c:K\to L$ be a morphism of ordinary bounded-below derived étale module
complexes. If $a^*c$ and the direct image $Rb_*c$ are isomorphisms, then $c$
is an isomorphism.

## Proof

Let $M$ be the cone of $c$. Its restriction to $G$ is zero. The termwise
localization sequence for extension by zero, verified on stalks, identifies
$M=i_*i^*M$. Therefore
$$
0=Rb_*M=R(bi)_*i^*M=(bi)_*i^*M,
$$
the last equality using exactness of finite direct image.

Finite direct image is conservative: its stalks are products over the finite
fibre, so a zero direct image forces every stalk on its source to be zero.
Apply this to every cohomology sheaf of $i^*M$. It follows that $i^*M=0$,
hence $M=0$ and $c$ is an isomorphism.

Unresolved dependencies: def:weil-pbc-scheme-conventions, def:weil-pbc-derived-categories, def:weil-pbc-direct-image, def:weil-pbc-extension-by-zero, lem:weil-pbc-geometric-stalk-conservative, lem:weil-pbc-finite-direct-image-exact, lem:weil-pbc-finite-stalk-formula
