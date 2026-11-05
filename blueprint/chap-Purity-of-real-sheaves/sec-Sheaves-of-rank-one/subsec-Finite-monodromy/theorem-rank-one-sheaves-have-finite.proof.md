+++
kind = "proof"
of = "theorem-rank-one-sheaves-have-finite"
order = 1108
uses = ["lemma-acyclic-resolutions", "lemma-proper-smooth-model", "proposition-kummer-duality-integral-tate-module", "lemma-schematic-closure-uniqueness", "theorem-theorem-cube", "lemma-symmetric-ample-sheaf", "proposition-multiplication-n", "proposition-integral-tate-module", "definition-relative-picard-functor", "lemma-rigidification-along-section", "lemma-twisting-h-0-1-h"]
+++
We show that a fixed power of $\chi$ is trivial on $\pi_1(U)$, by
applying Lemma [lemma-invariant-additive-characters] to its logarithm.
For this we need a subgroup $1+\mathfrak m_E^r$ of finite index in
$\mathcal O_E^\times$ on which the logarithm is an injective homomorphism,
and a power of $\chi$ that lands in it.

*Step 1: the logarithm.* The compact group
$\chi(\pi_1(U))$ lies in $\mathcal O_E^\times$, because its image under the normalized
valuation is a finite subgroup of $\mathbf Z$ and therefore zero.
Now write $e=v_E(\ell)$ and choose an integer
$r>e/(\ell-1)$. We claim that $\log$ is injective on $1+\mathfrak m_E^r$.
For $x\in\mathfrak m_E^r$ and $n\ge1$ we have
$v_E(n)=e\,v_\ell(n)$ and, by Legendre's formula,
$v_\ell(n!)\le(n-1)/(\ell-1)$, so that

$$
v_E(x^n/n)\ge nr-e\,v_\ell(n),
\qquad
v_E(x^n/n!)\ge r+(n-1)\bigl(r-e/(\ell-1)\bigr).
$$

Both bounds tend to infinity with $n$ and are at least $r$: for the
second this is clear, and for the first it follows from
$n-1\ge\ell^{v_\ell(n)}-1\ge(\ell-1)v_\ell(n)$ and $(\ell-1)r>e$, which
give $(n-1)r\ge e\,v_\ell(n)$. The logarithm and exponential
series therefore converge on $\mathfrak m_E^r$; the logarithm maps
$1+\mathfrak m_E^r$ into $\mathfrak m_E^r$, and the exponential maps
$\mathfrak m_E^r$ into $1+\mathfrak m_E^r$. By the usual identities of formal
power series, $\log:1+\mathfrak m_E^r\to\mathfrak m_E^r$ and $\exp$ are
mutually inverse continuous group homomorphisms.

*Step 2: a power of $\chi$.* The quotient
$\mathcal O_E^\times/(1+\mathfrak m_E^r)$ is finite, being isomorphic to
$(\mathcal O_E/\mathfrak m_E^r)^\times$; let $N>0$ be an integer that
kills it. As $\chi(\pi_1(U))\subset\mathcal O_E^\times$, we have
$\chi(g)^N\in1+\mathfrak m_E^r$ for $g\in\pi_1(U)$. Hence
$a(g)=\log(\chi(g)^N)$ defines a continuous homomorphism
$\pi_1(U)\to E$, which is invariant under conjugation by $s$ because $\chi$ takes
values in an abelian group.

*Step 3: conclusion.* Lemma [lemma-invariant-additive-characters]
gives $a=0$, so $\chi(g)^N=1$ for every $g\in\pi_1(U)$, the logarithm being
injective. The theorem follows, since $T^N-1$ has only finitely many roots
in $E$.
