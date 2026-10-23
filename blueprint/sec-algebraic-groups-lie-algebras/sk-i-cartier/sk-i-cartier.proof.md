+++
kind  = "proof"
of    = "sk-i-cartier"
+++
We first show that the reduced subscheme $G_{\mathrm{red}}$ is a smooth
group scheme. Since $L$ is perfect, products of reduced schemes of finite
type over $L$ are reduced
([Stacks 035Z](https://stacks.math.columbia.edu/tag/035Z)). A morphism
from a reduced scheme to $G$ factors through $G_{\mathrm{red}}$, and hence
multiplication and inversion restrict to $G_{\mathrm{red}}$. By
[Stacks 056V](https://stacks.math.columbia.edu/tag/056V), the reduced
scheme $G_{\mathrm{red}}$ contains a dense smooth open subscheme. Choose a
closed point in it. Since translations carry this point to any other
closed point of $G_{\mathrm{red}}$, we see that $G_{\mathrm{red}}$ is
smooth everywhere.

It remains to show that $G$ is not a nontrivial thickening of
$G_{\mathrm{red}}$. Let $A=\mathcal O_{G,1}$, with maximal ideal
$\mathfrak m$ and nilradical $I$, and let $\widehat A$ be its completion.
Multiplication at $(1,1)$ gives a continuous comultiplication

$$
\Delta:\widehat A\longrightarrow
\widehat A\,\widehat\otimes_L\widehat A.
$$

The counit is evaluation at $1$. We claim that $I\subseteq\mathfrak m^2$.
Since completion is faithfully flat, it suffices to prove that every
nilpotent $b\in\widehat A$ lies in $\widehat{\mathfrak m}^{\,2}$. Suppose
that $b\notin\widehat{\mathfrak m}^{\,2}$, and let $n\ge2$ be the least
integer with $b^n=0$. By the counit identities,

$$
\Delta(b)=b\otimes1+1\otimes b+w,
\qquad
w\in\widehat{\mathfrak m}\,\widehat\otimes_L\widehat{\mathfrak m}.
$$

We reduce the second factor modulo $\widehat{\mathfrak m}^{\,2}$. Then
every term in the binomial expansion of $\Delta(b)^n$ with two factors from
$1\otimes b+w$ vanishes. Since $b^n=0$, we are left with

$$
n b^{n-1}\otimes b+n(b^{n-1}\otimes1)w=0.
$$

If we now also reduce the first factor modulo
$b^{n-1}\widehat{\mathfrak m}$, the second term vanishes, and we get

$$
n\,\overline{b^{n-1}}\otimes\overline b=0
\quad\text{in}\quad
(\widehat A/b^{n-1}\widehat{\mathfrak m})
\otimes_L(\widehat A/\widehat{\mathfrak m}^{\,2}).
$$

Here $\overline{b^{n-1}}\ne0$ by Nakayama's lemma applied to the cyclic
module $(b^{n-1})$, which is nonzero by the choice of $n$, and
$\overline b\ne0$ by assumption. Since a tensor product of nonzero vectors
over a field is nonzero and $n\ne0$ in characteristic zero, this is a
contradiction.

It follows that $G$ and $G_{\mathrm{red}}$ have the same cotangent space
at $1$. They also have the same local dimension at $1$, and the local ring
of $G_{\mathrm{red}}$ at $1$ is regular. Hence

$$
\dim_L\mathfrak m/\mathfrak m^2=\dim A,
$$

so that $A$ is regular, and in particular a domain
([Stacks 00NP](https://stacks.math.columbia.edu/tag/00NP)). By
translation, the local rings of $G$ at all closed points are regular.
Since the nonsmooth locus is closed and contains no closed point, it is
empty. Thus $G$ is smooth, hence reduced, and its tangent space at $1$ has
dimension $\dim G$. Since $G^\circ$ is open in $G$, it has the same tangent
space at $1$.

For the complement: over an arbitrary field of characteristic zero,
reducedness and smoothness descend from the algebraic closure along the
faithfully flat base change
([Stacks 02VL](https://stacks.math.columbia.edu/tag/02VL)), and
$\dim\Lie(G)$ and $\dim G$ do not change; the local-finite-type case is the
same argument on affine opens. Restricting to the open neighbourhood
$G^\circ$ of $1$ changes neither the local ring nor its cotangent space.
Finally, dual-number points of $G\times G$ are pairs, and
$(1+\varepsilon X)(1+\varepsilon Y)=1+\varepsilon(X+Y)$ since
$\varepsilon^2=0$; for a general group scheme the counit identities give
the same computation.
