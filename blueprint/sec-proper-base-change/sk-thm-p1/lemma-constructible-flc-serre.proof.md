+++
kind  = "proof"
of    = "lemma-constructible-flc-serre"
uses = ["def-constructible-constant", "def-constructible-finite", "def-constructible-locally-constant", "def-pc-separably-closed", "lemma-constructible-flc-biproduct", "lemma-constructible-hom-constant-locally", "lemma-constructible-iso-invariance", "lemma-constructible-pullback-constant", "lemma-constructible-pullback-finite", "lemma-constructible-pullback-locally-constant"]
+++
Restricting to an étale cover trivialising both sheaves
([lemma-constructible-flc-biproduct]), we may assume the morphism is
$\varphi\colon M_X\to N_X$ with $M$, $N$ finitely generated (the stalks of
the constant sheaf $M_X$ are $M$). By [lemma-constructible-hom-constant-locally]
$\varphi$ is étale locally induced by a linear map $f\colon M\to N$, so
kernel and cokernel are étale locally the constant sheaves at $\ker f$ and
$\operatorname{coker}f$. The module $\operatorname{coker}f$ is finitely
generated as a quotient of $N$; the module $\ker f$ is finitely generated
when $\Lambda$ is Noetherian, as a submodule of the finitely generated module
$M$.

For an extension $0\to\mathcal E'\to\mathcal E\to\mathcal E''\to0$ with
$\Lambda$ finite and outer terms finite locally constant, work on an étale
cover on which $\mathcal E'\cong M_X$ and $\mathcal E''\cong N_X$ with $M$,
$N$ finitely generated, hence finite. Choose a surjection
$p\colon\Lambda^b\to N$ with kernel $K$, a finite module. Since
$\mathcal E\to N_X$ is an epimorphism of sheaves, it is locally surjective on
sections, so after refining the cover the images under $p$ of the $b$ basis
vectors lift to sections $y_1,\dots,y_b$ of $\mathcal E$. For $k\in K$ the
section $\sum_ik_iy_i$ maps to zero in $N_X$, hence is a section of
$M_X$; as $K$ is finite, after a further refinement all these finitely many
sections are constant, and $k\mapsto\sum_ik_iy_i$ is the constant map at a
linear map $\alpha\colon K\to M$. Let $L=M\amalg_K\Lambda^b$ be the pushout
of $\alpha$ and the inclusion $K\to\Lambda^b$; then
$0\to M\to L\to N\to0$ is exact, and the sections $y_i$ together with
$M_X\to\mathcal E$ define a morphism from the constant short exact sequence
$0\to M_X\to L_X\to N_X\to0$ to $0\to M_X\to\mathcal E\to N_X\to0$ which is
the identity on the outer terms. By the five lemma $L_X\cong\mathcal E$
there. Hence $\mathcal E$ is locally constant, with finite stalks $L$.
(An extension of finite constant sheaves need not be étale locally split:
for $\Lambda=\mathbf Z/4$ the constant extension
$0\to\mathbf Z/2\to\mathbf Z/4\to\mathbf Z/2\to0$ splits on no nonempty
étale scheme; this is why one passes through the pushout $L$.)
