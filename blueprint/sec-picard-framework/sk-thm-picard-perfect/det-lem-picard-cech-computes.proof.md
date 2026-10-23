+++
kind  = "proof"
of    = "det-lem-picard-cech-computes"
+++
*Step 1 (the intersections are affine).* For two affine opens
$U,V\subseteq X$ the intersection $U\cap V$ is the preimage of $U\times V$
under the diagonal of $X$; separatedness makes the diagonal a closed
immersion, and $U\times V$ is affine over the affine base, so $U\cap V$
is a closed subscheme of an affine scheme, hence affine. Iterating,
every $U_{i_0\dots i_p}=U_{i_0}\cap\dots\cap U_{i_p}$ is affine.

*Step 2 (the spectral sequence collapses).* Feed $\mathfrak U$ to
[det-thm-picard-cech]. For $q>0$ the presheaf $\mathcal H^q(\cF)$
vanishes on each $U_{i_0\dots i_p}$ by Step 1 and
[det-lem-picard-affine], so $E_2^{p,q}=\Cech^p(\mathfrak U,\mathcal H^q(\cF))=0$ for $q>0$. Only the row $q=0$ survives, the
sequence degenerates, and the edge maps
$\Cech^q(\mathfrak U,\cF)\to H^q(X,\cF)$ are isomorphisms in every
degree; this is the collapse described in Step 4 of the proof of
[det-thm-picard-cech].

*Step 3 (linearity).* Both sides are $\Gamma(X,\cO_X)$-modules, hence
$A$-modules through $A\to\Gamma(X,\cO_X)$, an element
$a\in\Gamma(X,\cO_X)$ acting by functoriality through the endomorphism
$a\cdot\colon\cF\to\cF$ of $\cO_X$-modules;
the spectral sequence of [det-thm-picard-cech], hence its edge map,
is natural in $\cF$, so the edge map commutes with these endomorphisms
and is $\Gamma(X,\cO_X)$-linear, hence $A$-linear.

This is Stacks, Cohomology of Schemes, Lemma 30.2.6
([`01XD`](https://stacks.math.columbia.edu/tag/01XD)); the detailed form is [lem-pc-cech-computes].
