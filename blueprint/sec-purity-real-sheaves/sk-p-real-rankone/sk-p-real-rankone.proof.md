+++
kind  = "proof"
of    = "sk-p-real-rankone"
uses = ["det-d-real-log"]
+++
The compact group $\chi(P)$ lies in $\mathcal O_E^\times$, because its
image under the normalized valuation is a finite subgroup of
$\mathbf Z$ and therefore zero. Write $e=v_E(\ell)$ and choose an integer
$r>e/(\ell-1)$. On $\mathfrak m_E^r$ the exponential and logarithm
series converge, since

$$
 v_E(x^n/n)\ge nr-e v_\ell(n)\longrightarrow\infty,
 \qquad
 v_E(x^n/n!)\ge n(r-e/(\ell-1))\longrightarrow\infty.
$$

By the usual identities of formal power series,
$\log:1+\mathfrak m_E^r\to\mathfrak m_E^r$ and $\exp$ are mutually
inverse continuous group homomorphisms; in particular, the logarithm
is injective on $1+\mathfrak m_E^r$ ([det-d-real-log],
[lem-wf-deep-principal-unit-log]).

The quotient $\mathcal O_E^\times/(1+\mathfrak m_E^r)$ is finite; let
$N>0$ be an integer that kills it. Then $a(g)=\log(\chi(g)^N)$
defines a continuous additive map $P\to E$
([lem-wf-compact-character-logarithm]). Since $\chi$ takes values in an
abelian group, this map is invariant under conjugation by $s$, and so $a=0$
by [sk-lem-wrp-additive]. As the logarithm is injective, we conclude that
$\chi(g)^N=1$ for every $g\in P$. The theorem follows, since $T^N-1$ has only
finitely many roots in $E$ ([thm-wf-rank-one-finite-geometric-image-curve]).
