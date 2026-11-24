+++
kind = "proof"
of = "lemma-ext-bound-lattices"
order = 445
+++
We first bound the complex in (3.1) for the torsion
reductions of $b_!M_0$ by [cohomological dimensions](@definition-cohomological-dimension), and then pass to the
derived limit, which costs one degree. Both [cohomological dimensions](@definition-cohomological-dimension) are
finite by [Stacks, [0F10](https://stacks.math.columbia.edu/tag/0F10)] and
Lemma [lemma-cohomological-dimension-base-field].

By Lemma [lemma-integral-models](3) and (4), $b_!M_0$ lies in
[$\Dbc(X,\mathcal O_E)$](@definition-constructible-sheaves), so it is [derived complete](@definition-derived-adic-completeness). Since $b_!$ is exact
and $M_0$ is $\pi_E$-torsion free, its reductions are

$$
b_!M_0\otimes^{\mathbf L}_{\href{@lemma-comparison-completed-coefficients}{\mathcal O_{E,X}}}\href{@lemma-comparison-completed-coefficients}{\mathcal O_{E,X}}/\pi_E^n
=b_!(M_0/\pi_E^n).
$$

These are [constructible](@definition-constructible-sheaves) [torsion sheaves](@definition-torsion-sheaves). They are pulled back from
$X_{\acute{e}t}$, because extension by zero and closed direct image commute with
this pullback [Stacks, [09AF](https://stacks.math.columbia.edu/tag/09AF), [09A6](https://stacks.math.columbia.edu/tag/09A6)].

*Torsion targets.* We bound the complex that appears in
(3.1) when the target is one of the [torsion sheaves](@definition-torsion-sheaves)
$b_!(M_0/\pi_E^n)$. By [Stacks, [09A6](https://stacks.math.columbia.edu/tag/09A6)], $Rj_*$ in
$D(\href{@definition-small-pro-etale-site}{X_{\mathrm{pro}\acute{e}t}},\mathcal O_E/\pi_E^n)$ of a sheaf pulled back from the
étale site is the pullback of its direct image in
$D(X_{\acute{e}t},\mathcal O_E/\pi_E^n)$. On the étale site the degrees are
controlled by the [cohomological dimension](@definition-cohomological-dimension), and hence
$Rj_*j^*b_!(M_0/\pi_E^n)$ has cohomology in degrees
$[0,\href{@definition-cohomological-dimension}{\operatorname{cd}_\ell(j)}]$. The fibre of the map from a sheaf to
this complex lives in degrees $[0,\href{@definition-cohomological-dimension}{\operatorname{cd}_\ell(j)}+1]$, so the
fibre formula of Lemma [lemma-sections-support-closed-subscheme](1) shows that

$$
\href{@definition-local-cohomology}{R\underline\Gamma_Z}\,b_!(M_0/\pi_E^n)\in D^{[0,\href{@definition-cohomological-dimension}{\operatorname{cd}_\ell(j)}+1]}(\href{@definition-small-pro-etale-site}{Z_{\mathrm{pro}\acute{e}t}},\mathcal O_E/\pi_E^n),
$$

and its cohomology sheaves are [torsion sheaves](@definition-torsion-sheaves) pulled back from the
étale site, though not necessarily [constructible](@definition-constructible-sheaves). Restricting to $S$
and tensoring with the locally free [lisse sheaf](@definition-lisse-sheaves) $L_0^\vee/\pi_E^n$
does not change this range of degrees. Since the cohomology of $S$ with
coefficients in a [torsion sheaf](@definition-torsion-sheaves) vanishes above [$\operatorname{cd}_\ell(S)$](@definition-cohomological-dimension),
the hypercohomology spectral sequence on $S$ gives

$$
H^q R\Gamma\bigl(S,(L_0^\vee/\pi_E^n)\otimes u^*\href{@definition-local-cohomology}{R\underline\Gamma_Z}\,b_!(M_0/\pi_E^n)\bigr)=0
\quad(q>\href{@definition-cohomological-dimension}{\operatorname{cd}_\ell(j)}+\href{@definition-cohomological-dimension}{\operatorname{cd}_\ell(S)}+1),
\tag{5.2}
$$

for every $n$, $b$ and $M_0$.

*Integral targets.* For the lattice $b_!M_0$ itself we write the
relevant complex as a derived limit of its reductions modulo $\pi_E^n$. Consider the complex
$L_0^\vee\otimes u^*\href{@definition-local-cohomology}{R\underline\Gamma_Z}\,b_!M_0$.
By Lemma [lemma-limits-sections-support], the functors that form it
commute with derived inverse limits of sequences. They also commute with
reduction modulo $\pi_E^n$, which is the cone of multiplication by
$\pi_E^n$. Since $b_!M_0$ is [derived complete](@definition-derived-adic-completeness), so is this complex, and
its reductions are the complexes in (5.2).
In other words, the complex is the derived limit of its reductions, and
we may compute its cohomology on $S$ from theirs.
Derived global sections preserve products and cones, and hence derived
inverse limits. Using (3.1) with $\mathcal O_E$
coefficients, that is, for $R\!\operatorname{Hom}$ in $D(\href{@definition-small-pro-etale-site}{X_{\mathrm{pro}\acute{e}t}},\mathcal O_E)$, we get

$$
R\!\operatorname{Hom}_X(a_!L_0,b_!M_0)
=R\Gamma\bigl(S,L_0^\vee\otimes u^*\href{@definition-local-cohomology}{R\underline\Gamma_Z}\,b_!M_0\bigr)
=R\varprojlim_n R\Gamma\bigl(S,(L_0^\vee\otimes u^*\href{@definition-local-cohomology}{R\underline\Gamma_Z}\,b_!M_0)\otimes^{\mathbf L}\mathcal O_E/\pi_E^n\bigr).
$$

A derived inverse limit of a sequence raises an upper bound on cohomology
by at most one. Indeed, it is the fibre of the difference of the identity and the
transition maps on the product, and
products of abelian groups are exact. This is the Milnor sequence
[Stacks, [08TB](https://stacks.math.columbia.edu/tag/08TB)]. Applied to the bound (5.2)
for the reductions, it gives (5.1).
