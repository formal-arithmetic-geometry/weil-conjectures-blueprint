+++
kind = "proof"
of = "det-sp-reduction-tower-normalized"
uses = ["sk-lem-int-integral-heart"]
+++
*Construction.* Choose a functorial K-flat representative $P$ of $M$ over
$\mathcal O_{E,T}$. The strict complexes $P\otimes_{\mathcal O_{E,T}}\mathcal O_{E,T}/\ell^n$
with the maps induced by the quotients
$\mathcal O_{E,T}/\ell^{n+1}\to\mathcal O_{E,T}/\ell^n$ form a complex of towers,
defining $\operatorname{red}_TM\in D(\operatorname{Tow}(T,\mathcal O_E))$; quasi-isomorphisms
of K-flat complexes give levelwise quasi-isomorphisms, so this is functorial in
$M$. Its level $n$ is $M/\ell^n$ by exactness of evaluation
([det-sp-coefficient-towers-abelian]).

*Normalization.* For $m\leq n$, the reduction map is the associativity
isomorphism
$(P\otimes\mathcal O_{E,T}/\ell^n)\otimes_{\mathcal O_{E,T}/\ell^n}\mathcal O_{E,T}/\ell^m
\cong P\otimes\mathcal O_{E,T}/\ell^m$ (the left side computes the derived
tensor product, $P\otimes\mathcal O_{E,T}/\ell^n$ being K-flat over
$\mathcal O_{E,T}/\ell^n$), hence an isomorphism.

*Constructibility.* Let $M\in\Dbc(T,\mathcal O_E)$. By [sk-lem-int-integral-heart],
$M$ is a finite extension of shifted sheaves $a_!C$ with $C$ of Tor amplitude
$[-1,0]$ on a stratum. Tor amplitude and constructibility of the reductions are
preserved by extensions and shifts, and the number of steps and the shifts do
not depend on $n$. Hence $M$ has finite Tor amplitude, say in $[a,b]$, and each
$M/\ell^n$ lies in $\Dctf(T_{\mathrm{proét}},\mathcal O_E/\ell^n)$ with Tor amplitude
in $[a,b]$. Since $M/\ell^n$ has
Tor amplitude in $[a,b]$ and is bounded, its cohomology lies in $[a,b]$ as
well (Tor amplitude in $[a,b]$ forces the cohomology to vanish outside it).
So the cohomological and Tor bounds are independent of $n$.
