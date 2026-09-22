+++
id = "the-decomposition-chain"
kind = "section"
title = "The decomposition chain"
order = 4376
+++
The chain that assembles the representability theorem. Base changes of $X$
stay smooth projective curves [prop-pc-XK-integral], so the Hilbert schemes
exist. The Picard sequence is exact [lem-pc-pic-exact], the kernel of
$\sigma^*$ is an fppf sheaf [lem-pc-k-sheaf], and together these split the
sequence [thm-pc-pic-split]; a curve with a rational point satisfies the
hypotheses [lem-pc-rational-hyp], whence
$\operatorname{Pic}_{X/k,\sigma}\cong\operatorname{Pic}_{X/k}$
[cor-pc-sigma-pic-iso].

The subfunctor $F$ where $Rf_*\mathcal L$ is invertible in degree $0$ is
open [lem-pc-f-open-subfunctor]; the zero scheme of the adjoint section is
a relative effective Cartier divisor of degree $g$
[lem-pc-zero-scheme-recd], and on the Hilbert scheme this section is the
canonical one [lem-pc-universal-adjoint-section]. Hence $F$ is represented
by an open subscheme of $\underline{\operatorname{Hilb}}^g_{X/k}$
[thm-pc-f-representable]. The twist lemma [lem-pc-twist] supplies the
translation needed by the representability criterion [thm-pc-criterion],
which converts an open representable subfunctor plus translations into a
group scheme.
