+++
kind  = "proof"
of    = "sk-r-real-linear"
uses = ["det-p-cyclotomic"]
+++
In a basis adapted to an invariant subspace, a matrix is block upper
triangular, and its characteristic polynomial is the product of those
on the subspace and on the quotient ([sk-p-linear-filtration]). Thus the
eigenvalues of either occur among those of the original matrix. For the
subquotient assertions, we intersect a mixed filtration with a subobject, or
take its images in a quotient. To filter an extension, we first filter its
subobject and then take the inverse images of a filtration of its
quotient ([lem-a1-mixed-direct-summand]). Since the coefficients form a
field, the tensor product of two filtrations has as associated graded the
tensor product of the two associated gradeds. Its eigenvalues are products
of eigenvalues, and the eigenvalues on the dual are the inverses; this
proves the statements on tensor products and duals ([lem-tw-multiplicativity],
[lem-tw-dual-negation]). At a closed point of an inverse image, the Frobenius
is a positive power of the Frobenius at the image point, and the residue
field degree is multiplied by the same integer, which proves the assertion on
inverse images. Finally, $\mathcal H^i(K[r])=\mathcal H^{i+r}(K)$, and the
local eigenvalue of $\mathcal B_b$ at $x$ is $b^{d(x)}$
([lem-wf-constant-twist-weight]). For the Tate sheaf, recall that arithmetic
Frobenius acts on roots of unity by raising to the $q$th power
([sk-d-ab-field]), and geometric Frobenius is its inverse
([det-p-cyclotomic], [lem-wf-tate-twist-frobenius],
[lem-tw-tate-twist-weight-shift]).

*Complement.* By Jordan–Hölder ([sk-r-linear-library]) and the
multiplicativity of characteristic polynomials along a filtration, a
semisimplification has the same local polynomials; the weight of
$\alpha^{-1}$ is the negative of that of $\alpha$ because
$|\iota(\alpha^{-1})|=|\iota(\alpha)|^{-1}$.
