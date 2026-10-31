+++
kind = "proof"
of = "sk-i-cartier"
+++
We first show that the reduced subscheme $G_{\mathrm{red}}$ is a smooth
group scheme. Since $\Omega$ is perfect, products of reduced schemes of
finite type over $\Omega$ are reduced [Stacks, Tag 035Z](https://stacks.math.columbia.edu/tag/035Z). A morphism from a
reduced scheme to $G$ factors through $G_{\mathrm{red}}$, and hence
multiplication and inversion restrict to $G_{\mathrm{red}}$. By
[Stacks, Tag 056V](https://stacks.math.columbia.edu/tag/056V), the reduced scheme $G_{\mathrm{red}}$ contains a dense
smooth open subscheme. Choose a closed point in it. Since translations
carry this point to any other closed point of $G_{\mathrm{red}}$, we see
that $G_{\mathrm{red}}$ is smooth everywhere.

It remains to show that $G$ is not a nontrivial thickening of
$G_{\mathrm{red}}$. Let
$R=\mathcal O_{G,1}$, with maximal ideal $\mathfrak m$ and nilradical
$I$, and let $\widehat R$ be its completion. Multiplication at
$(1,1)$ gives a continuous comultiplication

$$
\Delta:\widehat R\longrightarrow
\widehat R\,\widehat\otimes_\Omega\widehat R.
$$

The counit is evaluation at $1$. We claim that $I\subseteq\mathfrak m^2$.
Since completion is faithfully flat, it suffices to prove that every
nilpotent $b\in\widehat R$ lies in $\widehat{\mathfrak m}^{\,2}$.
Suppose that $b\notin\widehat{\mathfrak m}^{\,2}$, and let $n\ge2$ be
the least integer with $b^n=0$. By the counit identities,

$$
\Delta(b)=b\otimes1+1\otimes b+w,
\qquad
w\in\widehat{\mathfrak m}\,\widehat\otimes_\Omega
\widehat{\mathfrak m}.
$$

We reduce the second factor modulo $\widehat{\mathfrak m}^{\,2}$.
Then every term in the binomial expansion of $\Delta(b)^n$ with two
factors from $1\otimes b+w$ vanishes. Since $b^n=0$, we are left with

$$
n b^{n-1}\otimes b+n(b^{n-1}\otimes1)w=0.
$$

If we now also reduce the first factor modulo
$b^{n-1}\widehat{\mathfrak m}$, the second term vanishes, and we get

$$
n\,\overline{b^{n-1}}\otimes\overline b=0
\quad\text{in}\quad
(\widehat R/b^{n-1}\widehat{\mathfrak m})
\otimes_\Omega(\widehat R/\widehat{\mathfrak m}^{\,2}).
$$

Here $\overline{b^{n-1}}\ne0$ by Nakayama's lemma applied to the cyclic
module $(b^{n-1})$, which is nonzero by the choice of $n$, and
$\overline b\ne0$ by assumption. Since a tensor product of nonzero
vectors over a field is nonzero and $n\ne0$ in characteristic zero,
this is a contradiction.

It follows that $G$ and $G_{\mathrm{red}}$ have the same cotangent space
at $1$, since the kernel of
$\mathfrak m/\mathfrak m^2\to(\mathfrak m/I)/(\mathfrak m/I)^2$ is
$(I+\mathfrak m^2)/\mathfrak m^2=0$. They also have the same local
dimension at $1$, and the local ring $R/I$ of $G_{\mathrm{red}}$ at $1$
is regular. Hence

$$
\dim_\Omega\mathfrak m/\mathfrak m^2=\dim R,
$$

so that $R$ is regular, and in particular a domain [Stacks, Tag 00NP](https://stacks.math.columbia.edu/tag/00NP).
By translation, the local rings of $G$ at all closed points are
regular. Since $\Omega$ is perfect, $G$ is therefore smooth at every closed
point. As the nonsmooth locus is closed and contains no closed point, it
is empty. Thus $G$ is smooth, hence reduced, and its tangent
space at $1$ has dimension $\dim G$. Since $G^\circ$ is open in $G$, it
has the same tangent space at $1$.
