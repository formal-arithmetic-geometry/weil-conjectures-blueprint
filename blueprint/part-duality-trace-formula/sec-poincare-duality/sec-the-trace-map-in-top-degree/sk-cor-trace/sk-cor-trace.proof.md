+++
kind = "proof"
of = "sk-cor-trace"
uses = ["sk-thm-sf-identification", "sk-prop-scalar-six", "sk-def-ops", "sk-lem-geo-cartier", "sk-thm-regular", "sk-thm-smooth-purity", "sk-thm-purity-transport", "sk-thm-derived-duality", "sk-def-trace-cup", "sk-def-cd"]
+++
We read off the top degree from Poincaré duality in degree zero
over $\mathbf Z/\ell^n$, and then change coefficients. With finite coefficients, étale cohomology of a $d$-dimensional
scheme of finite type over an algebraically closed field vanishes above
degree $2d$, that is, $\operatorname{cd}_\ell(X)\le2d$ in the
notation of Definition [sk-def-cd] (SGA4, X, Cor. 4.3).
Since $X$ is connected, $H^0=\Lambda$. First let
$\Lambda=\mathbf Z/\ell^n$. This ring is injective as a module over
itself, so
$R\!\operatorname{Hom}_{\mathbf Z/\ell^n}(-,\mathbf Z/\ell^n)$ has cohomology equal to
the ordinary dual of the opposite cohomology. Poincaré
duality (Theorem [sk-thm-sf-identification]) in degree zero then identifies $H^{2d}(X,\mathbf Z/\ell^n(d))$
with $\Hom(H^0(X,\mathbf Z/\ell^n),\mathbf Z/\ell^n)=\mathbf Z/\ell^n$.
By Theorem [sk-thm-sf-identification] this identification is given by
pairing with $H^0$ and applying the trace map, so it is
$\operatorname{tr}_X(d)$.

Every finite $A$ is an algebra over some $\mathbf Z/\ell^n$. By
Proposition [sk-prop-scalar-six], the complexes with constant coefficients
and their traces over $A$ are obtained by derived extension of
scalars from $\mathbf Z/\ell^n$. For a complex with cohomology in
degrees $\le2d$, derived extension of scalars identifies the degree
$2d$ cohomology with the ordinary tensor product of the degree $2d$
cohomology. Hence the top cohomology is $A$, the trace is an
isomorphism, and the same upper bound holds.

For $\mathcal O_E$, we write $R\Gamma(X,\mathcal O_{E,X}(d))$ as the
derived inverse limit of the complexes $R\Gamma(X,(\mathcal O_E/\pi_E^n)_X(d))$. The cohomology groups at each level are finite,
so they satisfy the Mittag–Leffler condition and there is no $\lim^1$
contribution to the top group. Since the traces in top degree are
compatible, we get $H^{2d}(X,\mathcal O_{E,X}(d))=\mathcal O_E$, with the same
vanishing bounds. The lower bound and $H^0$
also follow directly from ordinary sheaf cohomology and
connectedness. Inverting $\ell$ and then extending scalars along
finite extensions of $E$, we obtain the cases $\Ql$, $E$ and $\overline{\mathbf Q}_\ell$.

It remains to treat the point class. Since exceptional adjunctions
compose, the composite of the counit for the closed point
with the trace map is the counit of $a_Xx=\mathrm{id}$, which takes
$1$ to $1$. Hence $\operatorname{tr}_X(d)([x])=1$.
