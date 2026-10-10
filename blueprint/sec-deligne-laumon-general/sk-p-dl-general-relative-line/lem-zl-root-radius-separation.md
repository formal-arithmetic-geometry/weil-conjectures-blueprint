+++
id = "lem-zl-root-radius-separation"
kind = "lemma"
title = "Separation by root radii"
order = 2837
lean = ["Polynomial.isCoprime_of_norm_inv_roots"]
+++
Let $A(T),B(T)\in\mathbf C[T]$ be nonzero, and let $R<S$ be real
numbers. If every root $z$ of $A$ satisfies $|z|^{-1}\le R$ and every
root $z$ of $B$ satisfies $|z|^{-1}=S$ (for a root $z=0$, read
$|z|^{-1}$ as $0$), then $A$ and $B$ are coprime.

## Proof

Over the algebraically closed field $\mathbf C$, two nonzero
polynomials are coprime if and only if they have no common root. A
common root $z$ would satisfy $S=|z|^{-1}\le R$, contradicting $R<S$.
Hence no root of $B$ is a root of $A$, and $A$ and $B$ are coprime.

In particular, if $A,B\in1+T\mathbf C[T]$, so that the numbers $z^{-1}$
are their reciprocal roots, no cancellation occurs in $A(T)/B(T)$: its
reciprocal poles of modulus $S$ are exactly the reciprocal roots of
$B$, with multiplicity.
