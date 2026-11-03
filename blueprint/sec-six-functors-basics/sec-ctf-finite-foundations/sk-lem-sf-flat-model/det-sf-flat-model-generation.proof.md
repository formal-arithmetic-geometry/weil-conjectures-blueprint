+++
kind = "proof"
of = "det-sf-flat-model-generation"
uses = ["lem-sf-flat-model"]
+++
*(1)* A constructible sheaf admits a finite partition into locally closed
constructible strata on which it is locally constant with finite stalks; by
Noetherian induction (take a dense open of the remaining closed set on which
the sheaf is locally constant, and continue on the complement) this partition
may be chosen with the stated ordering. The stalk $F_{\bar x}$ at a geometric
point is a finite $A$-module (constructibility) and flat (flatness of $F$ is
tested on stalks, filtered colimits of injections being injections). A finite
flat module over the Noetherian ring $A$ is finitely presented and flat, hence
projective.

*(2)* Induct on the number $m$ of strata. Let $U=S_1$, open in $X$, with
inclusion $j=a_1$, and $i:X_{\ge2}\hookrightarrow X$ the closed complement. The
open–closed sequence $0\to j_!j^*F\to F\to i_*i^*F\to0$ is exact, with
$j_!j^*F=a_{1!}L_1$; and $i^*F$ is flat constructible on $X_{\ge2}$ with the
induced partition into $m-1$ strata, so by induction it is an iterated
extension of $a'_{k!}L_k$ ($k\ge2$, $a'_k:S_k\to X_{\ge2}$), and $i_*$ (exact)
carries this to an iterated extension of $i_*a'_{k!}L_k=a_{k!}L_k$. Each
$a_{k!}L_k$ has stalks $0$ or finite projective, so it is flat constructible;
a flat sheaf in degree $0$ has Tor amplitude in $[0,0]$, so
$a_{k!}L_k\in\Dctf(X,A)$.

*(3)* Let $\mathcal G$ be the smallest full subcategory containing the objects
$a_!L$ and closed under shifts, cones and summands. By (2) each $a_!L$ lies in
$\Dctf(X,A)$, which is triangulated and closed under summands, so
$\mathcal G\subset\Dctf(X,A)$. Conversely let $C\in\Dctf(X,A)$; by the
constructible variant of [lem-sf-flat-model] it is represented by a bounded
complex $P$ of flat constructible sheaves, $P^q=0$ for $q\notin[a,b]$. The
stupid truncations $\sigma^{\ge q}P$ give distinguished triangles
$\sigma^{\ge q+1}P\to\sigma^{\ge q}P\to P^q[-q]\to$, so $C$ is a finite iterated
extension of the shifts $P^q[-q]$; each $P^q$ is, by (1) and (2), an iterated
extension of sheaves $a_!L$. Hence $C\in\mathcal G$.
