+++
kind = "proof"
of = "proposition-weights-under-usual-operations"
order = 1074
uses = ["lemma-subobjects-quotients-weil-sheaves"]
+++
Each assertion has two parts: a statement about eigenvalues at closed
points, which follows from Lemma [lemma-filtrations-spectra], and, for
mixedness, the construction of a filtration with pure quotients.

An extension is filtered by a filtration of its
subobject followed by the inverse images of a filtration of its
quotient. The graded pieces of the result are those of the two given
filtrations, so a common upper bound persists.

For tensor products we use that the coefficients form a field, so that the
associated graded of the tensor product of two filtrations is the tensor
product of the two associated gradeds. By
Lemma [lemma-filtrations-spectra], the eigenvalues of tensor
products and duals are the products $\alpha_i\beta_j$ and the
inverses $\alpha_i^{-1}$, whose weights are $a+b$ and $-a$.

For the dual of a mixed lisse sheaf $G$ with mixed filtration
$(G_i)$, suppose first that the graded pieces $G_i/G_{i-1}$ are lisse.
Dualizing is exact on lisse sheaves, so the annihilator filtration
$G_i^\perp=\ker(G^\vee\to G_i^\vee)$ has graded pieces
$(G_i/G_{i-1})^\vee$, which are pure of the negated weights by the
computation above. In general the graded pieces need not be lisse: on a
curve, a pure lisse $G$ has the filtration $j_!j^*G\subseteq G$, whose
quotient $i_*i^*G$ is a skyscraper with dual zero. We then argue by
Noetherian induction on $X$. Let $U\subseteq X$ be a dense open, stable
under Frobenius, on which all graded pieces are lisse, and let
$i:Z\to X$ be its closed complement. On $U$ the first case applies to
$j^*G$. Since $G$ is lisse, $i^*(G^\vee)\simeq(i^*G)^\vee$, and $i^*G$ is a
mixed lisse sheaf on $Z$, so $i^*(G^\vee)$ is mixed by induction, of the
negated weights. Extension by zero and direct image along a closed
immersion are exact and do not change stalks, so they carry mixed
filtrations to mixed filtrations of the same weights, and the exact
sequence

$$
0\to j_!j^*(G^\vee)\to G^\vee\to i_*i^*(G^\vee)\to 0
$$

shows that $G^\vee$ is mixed, of the negated weights.

Inverse images do not change weights, because the weight is normalized
by the degree. Indeed, at a closed point of an inverse image the Frobenius is a
positive power of the Frobenius at the image point, and the residue field
degree is multiplied by the same integer. For shifts, $\mathcal H^i(K[r])=\mathcal H^{i+r}(K)$ is mixed of weights
at most $w+i+r$, which is the bound $w+r$ for $K[r]$.

The local eigenvalue of $\mathcal B_b$ at $x$ is $b^{\deg(x)}$,
of weight $2\log_q|\iota(b)|$, and tensoring by $\mathcal B_b$ multiplies every
eigenvalue by it. For the Tate sheaf, recall that
arithmetic Frobenius acts on roots of unity by raising to the $q$th
power. Geometric Frobenius is its inverse, so it acts on
$\overline{\mathbf Q}_\ell(1)$ by $q^{-1}$, of weight $-2$.
