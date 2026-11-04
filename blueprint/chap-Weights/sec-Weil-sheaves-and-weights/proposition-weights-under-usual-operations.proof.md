+++
kind = "proof"
of = "proposition-weights-under-usual-operations"
order = 1065
uses = ["lemma-weights-exact-sequence"]
+++
Each assertion has two parts: a statement about eigenvalues at closed
points, which follows from Lemma [lemma-filtrations-spectra], and, for
mixedness, the construction of a filtration with pure quotients.

By Lemma [lemma-filtrations-spectra], the eigenvalues on a subobject or a
quotient occur among those of the whole. Hence subobjects and quotients of
pure sheaves are pure. Intersect a mixed filtration with a
subobject, or push it into a quotient. The graded pieces are then
subquotients of the original pure pieces, hence pure of the same
weights.  An extension is filtered by a filtration of its
subobject followed by the inverse images of a filtration of its
quotient. The graded pieces of the result are those of the two given
filtrations, so a common upper bound persists.

For tensor products we use that the coefficients form a field, so that the
associated graded of the tensor product of two filtrations is the tensor
product of the two associated gradeds. By
Lemma [lemma-filtrations-spectra], the eigenvalues of tensor
products and duals are the products $\alpha_i\beta_j$ and the
inverses $\alpha_i^{-1}$, whose weights are $a+b$ and $-a$.

Inverse images do not change weights, because the weight is normalized
by the degree. At a closed point of an inverse image the Frobenius is a
positive power of the Frobenius at the image point, and the residue field
degree is multiplied by the same integer. For shifts, $\mathcal H^i(K[r])=\mathcal H^{i+r}(K)$ is mixed of weights
at most $w+i+r$, which is the bound $w+r$ for $K[r]$.

The local eigenvalue of $\mathcal B_b$ at $x$ is $b^{\deg(x)}$,
of weight $2\log_q|\iota(b)|$. Tensoring by $\mathcal B_b$ multiplies every
eigenvalue by it. For the Tate sheaf, recall that
arithmetic Frobenius acts on roots of unity by raising to the $q$th
power. Geometric Frobenius is its inverse, so it acts on
$\overline{\mathbf Q}_\ell(1)$ by $q^{-1}$, of weight $-2$.
