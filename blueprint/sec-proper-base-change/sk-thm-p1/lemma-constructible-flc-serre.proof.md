+++
kind  = "proof"
of    = "lemma-constructible-flc-serre"
uses = ["def-constructible-constant", "def-constructible-finite", "def-constructible-locally-constant", "def-pc-separably-closed", "lemma-constructible-hom-constant-locally", "lemma-constructible-iso-invariance", "lemma-constructible-pullback-constant", "lemma-constructible-pullback-finite", "lemma-constructible-pullback-locally-constant"]
+++
Restricting to an étale cover trivialising both sheaves
([lemma-constructible-flc-biproduct]), we may assume the morphism is
$\varphi\colon M_X\to N_X$ with $M$, $N$ finite (the stalks of the constant
sheaf $M_X$ are $M$). By [lemma-constructible-hom-constant-locally]
kernel and cokernel are locally constant with finite stalks.

For an extension $0\to M_X\to\mathcal E\to N_X\to0$, again on a
trivialising cover, consider the sheaf $P$ of sections of
$\mathcal E\to N_X$: over $U\to X$ its sections are the morphisms
$s\colon N_U\to\mathcal E|_U$ with $\pi\circ s=\mathrm{id}$. It is a torsor
under the sheaf $\mathcal{H}om(N_X,M_X)=\Hom_\Lambda(N,M)_X$ (two sections
differ by a morphism $N_U\to M_U$, and locally sections exist since the
sequence is locally split in the étale topology: the stalks are finite
modules and a surjection of sheaves is locally surjective on sections).
The group $\Hom_\Lambda(N,M)$ is finite, so by
[lemma-constructible-torsor-trivialises] $P$ has a section over an
étale cover $(U_i\to X)$, and over $U_i$ the sequence splits:
$\mathcal E|_{U_i}\cong M_{U_i}\oplus N_{U_i}=(M\oplus N)_{U_i}$. Hence
$\mathcal E$ is locally constant, with finite stalks $M\oplus N$.
