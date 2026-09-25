+++
id = "sk-thm-picard-serre-b"
kind = "section"
title = "Serre's theorem B: vanishing after a twist"
order = 630
uses = ["sk-def-av-jacobian", "sk-def-av-pic"]
+++
*Theorem (sketch).*

Let $X\subseteq\PP^n_k$ be a closed subscheme and $\cF$ coherent on
$X$. Then $H^q(X,\cF\otimes\cO_X(m))=0$ for all $q>0$ and
$m\gg0$.

## Proof

By induction on $\dim X$ using
$0\to\cF(-1)\otimes\cO(m)\to\cF\otimes\cO(m)\to\cF|_Z\otimes \cO(m)\to0$ for a hypersurface $Z$ containing $X$ in dimension
degree, and [sk-thm-picard-pn] (ii): the only non-vanishing degree is
$q=n$, where [sk-thm-picard-pn] (iii) with $m\ge0$ gives $0$.
