+++
kind = "proof"
of = "sk-p-real-rankone"
uses = ["det-d-real-log"]
+++
We show that a fixed power of $\chi$ is trivial on $\pi_1(U)$, by
applying Lemma [sk-lem-wrp-additive] to its logarithm. The compact group
$\chi(\pi_1(U))$ lies in $\mathcal O_E^\times$, because its image under the normalized
valuation is a finite subgroup of $\mathbf Z$ and therefore zero.
Write $e=v_E(\ell)$ and choose an integer
$r>e/(\ell-1)$. For $x\in\mathfrak m_E^r$ and $n\ge1$ we have
$v_E(n)=e\,v_\ell(n)$ and, by Legendre's formula,
$v_\ell(n!)\le(n-1)/(\ell-1)$. Hence

$$
v_E(x^n/n)\ge nr-e\,v_\ell(n),
\qquad
v_E(x^n/n!)\ge r+(n-1)\bigl(r-e/(\ell-1)\bigr).
$$

Both bounds tend to infinity with $n$ and are at least $r$. For the
second this is clear. For the first, we have
$n-1\ge\ell^{v_\ell(n)}-1\ge(\ell-1)v_\ell(n)$ and $(\ell-1)r>e$, so
that $(n-1)r\ge e\,v_\ell(n)$. Therefore the logarithm and exponential
series converge on $\mathfrak m_E^r$, and they map $1+\mathfrak m_E^r$
into $\mathfrak m_E^r$ and $\mathfrak m_E^r$ into $1+\mathfrak m_E^r$.
By the usual identities of formal power series,
$\log:1+\mathfrak m_E^r\to\mathfrak m_E^r$ and $\exp$ are mutually
inverse continuous group homomorphisms. In particular, the logarithm
is injective on $1+\mathfrak m_E^r$.

The quotient $\mathcal O_E^\times/(1+\mathfrak m_E^r)$ is finite; let
$N>0$ be an integer that kills it. Since
$\chi(\pi_1(U))\subset\mathcal O_E^\times$, we have
$\chi(g)^N\in1+\mathfrak m_E^r$ for $g\in\pi_1(U)$, and
$a(g)=\log(\chi(g)^N)$ defines a continuous homomorphism
$\pi_1(U)\to E$. Since $\chi$ takes values
in an abelian group, this map is invariant under conjugation by $s$,
and hence $a=0$ by Lemma [sk-lem-wrp-additive]. As the logarithm is
injective, we conclude that $\chi(g)^N=1$ for every $g\in\pi_1(U)$. The
theorem follows, since $T^N-1$ has only finitely many roots in $E$.
