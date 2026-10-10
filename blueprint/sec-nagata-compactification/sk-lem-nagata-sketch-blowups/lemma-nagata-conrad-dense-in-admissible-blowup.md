+++
id = "lemma-nagata-conrad-dense-in-admissible-blowup"
kind = "lemma"
title = "Density in an admissible blow-up"
order = 175
lean = ["AlgebraicGeometry.IsAdmissible.dense_coe_preimage_blowupMap", "AlgebraicGeometry.IsAdmissible.dense_preimage_blowupMap_of_qcqs", "AlgebraicGeometry.Scheme.IdealSheafData.isSchemeTheoreticallyDominant_blowupMap_preimage_compl_support"]
uses = ["def-nagata-admissible-blowup", "def-nagata-dense-compactification", "def-nagata-global-blowup", "def-nagata-scheme-theoretically-dense-open", "lemma-nagata-admissible-blowup-preserves-density", "lemma-nagata-blowup-proper", "prop-nagata-global-blowup-cover-independent", "thm-nagata-blowup-principalizes-center", "thm-nagata-global-blowup-complement", "thm-nagata-global-blowup-proper"]
+++
Let $X$ be qcqs, let $U\subseteq X$ be an open subscheme, and let
$\pi\colon\widetilde X=\operatorname{Bl}_{\mathcal I}(X)\to X$ be a
$U$-admissible blow-up. If $D\subseteq X$ is a dense subset, then
$\pi^{-1}(D)$ is dense in $\widetilde X$; in particular, if $D$ is a dense
open subset of $X$, then $\pi^{-1}(D)$ is a dense open subset of
$\widetilde X$. If moreover $V(\mathcal I)=X\setminus U$, then
$\pi^{-1}(U)$ is scheme-theoretically dense in $\widetilde X$.

## Proof

Put $W=X\setminus V(\mathcal I)$. By the first assertion of
[lemma-nagata-admissible-blowup-preserves-density], $\pi^{-1}(W)$ is
scheme-theoretically dense in $\widetilde X$. A scheme-theoretically dense
open is topologically dense: if a non-empty open $O\subseteq\widetilde X$
missed $\pi^{-1}(W)$, the restriction map
$\mathcal O_{\widetilde X}(O)\to\mathcal O_{\widetilde X}(O\cap\pi^{-1}(W))=0$
would be injective, forcing $\mathcal O_{\widetilde X}(O)=0$, which is
impossible for a non-empty open. Moreover $\pi$ restricts over $W$ to an
isomorphism $\pi^{-1}(W)\xrightarrow{\sim}W$ by
[thm-nagata-global-blowup-complement].

Let $D\subseteq X$ be dense and let $O\subseteq\widetilde X$ be a non-empty
open. Then $O\cap\pi^{-1}(W)$ is a non-empty open of $\pi^{-1}(W)$, so its
image under the isomorphism $\pi^{-1}(W)\xrightarrow{\sim}W$ is a non-empty
open subset of $W$, hence of $X$. It therefore meets $D$ in some point
$\pi(y)$ with $y\in O\cap\pi^{-1}(W)$, and then $y\in O\cap\pi^{-1}(D)$.
Thus $\pi^{-1}(D)$ meets every non-empty open of $\widetilde X$, i.e. it is
dense. If $D$ is moreover open, $\pi^{-1}(D)$ is open by continuity.

If $V(\mathcal I)=X\setminus U$, then $W=U$, and the scheme-theoretic
density of $\pi^{-1}(U)=\pi^{-1}(W)$ was shown above.
