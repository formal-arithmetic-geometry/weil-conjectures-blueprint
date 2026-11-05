+++
kind = "proof"
of = "lemma-finite-cover-projective-space--1"
order = 392002
uses = []
+++
First construct the multiplication morphism

$$
\mu_k:\mathbf P^1_{\mathbf P^k_S}\longrightarrow\mathbf P^{k+1}_S
$$

from the coefficients of

$$
(xT+yU)\sum_{j=0}^kG_jT^jU^{k-j}.
$$

On each product chart, the coordinates of each factor generate the unit
ideal. Gauss' lemma for content ideals shows that the coefficients of
their product do so as well, and hence define a morphism. Over
$\Spec\Z$, these coefficients are linear forms in the Segre coordinates.
The inverse image of a standard affine open of the target is the inverse
image, under the Segre closed immersion, of the affine open where the
corresponding linear form does not vanish. Thus the multiplication
morphism is affine. It is also proper, since its source is proper and
its target separated over $\Spec\Z$, and is therefore finite. Base change
gives the finite morphism $\mu_k$ over $S$.

For surjectivity, over an algebraically closed field a nonzero
polynomial of degree at most $k+1$ is a product of a linear form and a
polynomial of degree at most $k$. For a nonconstant polynomial, choose
a root and divide by its monic linear factor; for a constant polynomial,
use the factor $1$, which corresponds to $U$ after homogenization.
Normalizing a nonzero coefficient of the remaining factor gives the
required projective points. This proves surjectivity over $\Spec\Z$,
and surjectivity is preserved by base change to $S$. The construction
also shows that $\mu_k$ is a morphism over $S$.

For $k=0$, the morphism $\sigma_{0,e}$ is the inverse of the isomorphism
$\pi_I:\mathbf P(I;S)\to S$, since $I$ has one element. For the
inductive step, first use the standard ordering of the $k+1$ coordinates
and then form the composite

$$
X_{k+1}=\mathbf P^1_{X_k}
\longrightarrow\mathbf P^1_{\mathbf P^k_S}
\xrightarrow{\mu_k}\mathbf P^{k+1}_S,
$$

with the target coordinates relabelled by $e$. The first arrow is the
base change of $\sigma_k$ along
$\mathbf P^1_{\mathbf P^k_S}\to\mathbf P^k_S$. By induction it is finite
and surjective, and composing with $\mu_k$ preserves both properties.
Compatibility with the projections follows from that of these two
arrows and the inductive identity $\pi\circ\sigma_k=p_k$.
