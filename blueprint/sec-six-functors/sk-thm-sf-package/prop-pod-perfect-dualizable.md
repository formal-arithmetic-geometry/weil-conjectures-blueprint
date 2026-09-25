+++
id = "prop-pod-perfect-dualizable"
kind = "theorem"
title = "Dualizability of a perfect complex"
order = 2391
tags = ["latex:proposition"]
uses = ["def-pod-conventions", "def-pod-perfect-complex-on-x", "def-weil-derived-pullback-tensor-hom", "def-weil-derived-tensor", "def-weil-geometric-hypotheses", "lem-pod-finite-projective-tensor-hom"]
+++
In the Poincare duality conventions of this chapter (the fixed setting),
$K\in D^b_{ctf}(X,\Lambda)$ be
perfect over $\Lambda_X$.
Then:

1. $K^\vee=R\mathcal Hom_X(K,\Lambda_X)$ is perfect over
$\Lambda_X$, and the canonical evaluation
$K\otimes^L_{\Lambda_X}K^\vee\to\Lambda_X$ is defined;
1. for every $M\in D^b_{ctf}(X,\Lambda)$ the canonical map
$$
K^\vee\otimes^L_{\Lambda_X}M\longrightarrow R\mathcal Hom_X(K,M)
$$
is an isomorphism (the tensor–internal-Hom adjunction in dualizable
form);
1. the canonical map $K\to K^{\vee\vee}$ is an isomorphism, and
$K^\vee\otimes^L_{\Lambda_X}K\to\Lambda_X$ and
$\Lambda_X\to K\otimes^L_{\Lambda_X}K^\vee$ are respectively the
evaluation and coevaluation of the duality;
1. the isomorphisms of (2) and (3) are compatible with finite
reduction, scalar extension, and shifts.

## Proof

Choose locally a bounded complex $P^\bullet$ of finite projective
$\Lambda_X$-modules with a quasi-isomorphism
$P^\bullet\to K$ ([def-pod-perfect-complex-on-x]), and let
$I(M)$ be a functorial K-injective replacement of $M$; since the
terms of $P^\bullet$ are projective,
$R\mathcal Hom_X(K,M)$ is represented by
$\mathcal Hom_X^\bullet(P^\bullet,I(M))$, by
[def-weil-derived-pullback-tensor-hom], and termwise
$\mathcal Hom_X(P^j,I(M)^k)=P^{j\vee}\otimes_{\Lambda_X}I(M)^k$ by
[lem-pod-finite-projective-tensor-hom], the identification being
compatible with the differentials. Hence
$R\mathcal Hom_X(K,M)\cong P^{\bullet\vee}\otimes_{\Lambda_X}I(M) \cong K^\vee\otimes^L_{\Lambda_X}M$, which proves (2); by (1) of the
same lemma the complex $P^{\bullet\vee}$ is again bounded with finite
projective terms, which proves (1). For (3), applying (2) twice gives
$K^{\vee\vee}\cong(P^{\bullet\vee})^{\vee}\cong P^\bullet\cong K$, the
middle identification being the termwise double-dual iso of
[lem-pod-finite-projective-tensor-hom], and the counit and the
coevaluation are the adjunction unit and counit of
[def-weil-derived-tensor], whose composition is the identity by
the triangle identities of the tensor–internal-Hom adjunction of
[def-weil-derived-pullback-tensor-hom]. Assertion (4) follows
from the functoriality of the K-flat and K-injective replacements and
of the tensor and internal Hom, in particular their compatibility with
finite reduction and scalar extension as recorded in
[def-weil-derived-pullback-tensor-hom].
