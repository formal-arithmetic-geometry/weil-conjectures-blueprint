+++
kind = "proof"
of = "proposition-w-local-components--2"
order = 45002
uses = ["definition-w-local-w-strictly-local--2", "proposition-w-local-components--1"]
+++
For the retained informal statement, let $C$ be the component of
$\mathfrak m$. Every point $\mathfrak p$ in $C$ specializes to a
closed point in $C$, which must be $\mathfrak m$ by
[proposition-w-local-components--1]. Conversely, any generalization
of $\mathfrak m$ lies in $C$. Thus $C$ consists exactly of the primes
$\mathfrak p\subseteq\mathfrak m$, which are the image of
$\operatorname{Spec}(R_{\mathfrak m})$. The localization map is a
homeomorphism onto this subspace. Lean uses the correspondence
between primes of a localization and primes contained in
$\mathfrak m$ directly, without a separate declaration identifying
this image with $C$.
