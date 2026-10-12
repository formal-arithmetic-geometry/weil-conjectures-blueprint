+++
kind  = "proof"
of    = "lemma-constructible-of-refines"
uses = ["lemma-constructible-immersion-independence"]
+++
Fix $l$ and choose $k$ with $X'_l\subseteq X_k$. The base change
$\kappa'_l\colon W_l\times_XZ_k\to Z_k$ of $\kappa_l$ is an immersion, and
the composite $\iota_k\circ\kappa'_l\colon W_l\times_XZ_k\to X$ is an
immersion with image $\iota_k(\iota_k^{-1}(X'_l))=X'_l$, the same image as
$\kappa_l$. Its pullback of $\mathcal F$ is
$\kappa_l'^*\iota_k^*\mathcal F$, finite locally constant by
[prop-constructible-pullback] (its lemmas for locally constant and
finite sheaves). By [lemma-constructible-immersion-independence],
$\kappa_l^*\mathcal F$ is finite locally constant. As $l$ was arbitrary, the
stratification $(\kappa_l)_l$ (and already $(\iota_k)_k$) witnesses that
$\mathcal F$ is constructible in the sense of [def-constructible-constructible].
