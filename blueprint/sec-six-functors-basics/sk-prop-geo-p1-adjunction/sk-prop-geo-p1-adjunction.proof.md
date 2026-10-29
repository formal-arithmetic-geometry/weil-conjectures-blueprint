+++
kind = "proof"
of = "sk-prop-geo-p1-adjunction"
uses = ["sk-lem-geo-cartier", "sk-lem-geo-p1-cohomology", "sk-lem-pbc-exchange-pasting"]
+++
As explained at the start of the subsection, we work on the étale sites of
$S$, $\mathbf P^1_S$ and $\mathbf P^1_S\times_S\mathbf P^1_S$, and transport
the unit and counit to the pro-étale site at the end.

Let $p_1,p_2:\mathbf P^1_S\times_S\mathbf P^1_S\to\mathbf P^1_S$ be the
projections and
$\Delta:\mathbf P^1_S\hookrightarrow\mathbf P^1_S\times_S\mathbf P^1_S$ the
diagonal. Let $x_0,x_1$ and $y_0,y_1$ be the pullbacks along $p_1$ and $p_2$
of the homogeneous coordinates of $\mathbf P^1_S$. Then $\Delta$ is the zero
locus of the section $x_0y_1-x_1y_0$ of
$p_1^*\mathcal O(1)\otimes p_2^*\mathcal O(1)$. On the open where $x_0$ and
$y_0$ are invertible, in the affine coordinates $x=x_1/x_0$ and $y=y_1/y_0$,
this equation becomes $y-x$, a nonzerodivisor with quotient
$\mathcal O_S[x,y]/(y-x)\simeq\mathcal O_S[x]$ flat over $S$. The open where
$x_1$ and $y_1$ are invertible is treated in the same way, and these two opens
cover $\Delta$. Hence $\Delta$ is a relative effective Cartier divisor, and it
remains one after every base change. [sk-lem-geo-cartier] provides its cycle
class

$$
\delta:\Delta_*\Lambda_{\mathbf P^1_S}\longrightarrow
  \Lambda_{\mathbf P^1_S\times_S\mathbf P^1_S}(1)[2].
$$

For $i=1,2$, the projection $p_i$ is a projective line over the other factor,
with trace $\operatorname{Tr}_{p_i}$ given by (G3) of
[sk-lem-geo-p1-cohomology]. Applying $Rp_{i*}$ to $\delta$ and then the trace,
we obtain an endomorphism

$$
s_i:\Lambda_{\mathbf P^1_S}=Rp_{i*}\Delta_*\Lambda_{\mathbf P^1_S}
      \xrightarrow{Rp_{i*}\delta}
      Rp_{i*}\Lambda_{\mathbf P^1_S\times_S\mathbf P^1_S}(1)[2]
      \xrightarrow{\operatorname{Tr}_{p_i}}\Lambda_{\mathbf P^1_S}. \qquad\text{(G5)}
$$

*Claim: $s_1=s_2=1$.* Both sides are endomorphisms of a sheaf placed in degree
zero, and we have

$$
\Hom_{D((\mathbf P^1_S)_{\mathrm{ét}},\Lambda)}(\Lambda_{\mathbf P^1_S},\Lambda_{\mathbf P^1_S})
  =\Hom_{\Mod((\mathbf P^1_S)_{\mathrm{ét}},\Lambda)}(\Lambda_{\mathbf P^1_S},\Lambda_{\mathbf P^1_S}),
$$

and hence $s_i$ is a morphism of sheaves and is determined by its geometric
stalks. By proper base change and the compatibility of $\delta$ and
$\operatorname{Tr}_{p_i}$ with base change, the stalk of (G5) at a geometric
point $\bar x$ of $\mathbf P^1_S$ is computed on the fibre
$p_i^{-1}(\bar x)\simeq\mathbf P^1_{\bar x}$. On this fibre the equation
$x_0y_1-x_1y_0$ restricts to a nonzero linear form, so the diagonal cuts out a
single reduced point, whose line bundle is $\mathcal O(1)$. By
[sk-lem-geo-cartier], the class of this point composed with the unit is
$c_1(\mathcal O(1))$, and $\operatorname{Tr}_p$ sends $c_1(\mathcal O(1))$ to
$1$ by the definition (G3) of the trace as the projection onto the summand of
(G2) spanned by this class. Hence the stalk of $s_i$ at $\bar x$ sends $1$ to
$1$, and since this holds at every geometric point, $s_i=1$.

*The unit and counit.* For $M\in D((\mathbf P^1_S)_{\mathrm{ét}},\Lambda)$, we
define

$$
\begin{aligned}
\eta_M:M
&=Rp_{2*}\Delta_*M\\
&\longrightarrow Rp_{2*}\bigl(p_1^*M(1)[2]\bigr)
  \xrightarrow{\ \sim\ }p^*Rp_*M(1)[2] .
\end{aligned}
\qquad\text{(G6)}
$$

Here the first arrow is $Rp_{2*}$ applied to $\delta\otimes p_1^*M$, where we
use the projection formula
$\Delta_*M=\Delta_*\Lambda\otimes^{\mathbf L}p_1^*M$, and the second is the
proper base change isomorphism $p^*Rp_*\simeq Rp_{2*}p_1^*$. For
$N\in D(S_{\mathrm{ét}},\Lambda)$, we define

$$
\varepsilon_N:Rp_*\bigl(p^*N(1)[2]\bigr)
  \xrightarrow{\ \sim\ }N\otimes_\Lambda^{\mathbf L}Rp_*\Lambda_{\mathbf P^1_S}(1)[2]
  \xrightarrow{1\otimes \operatorname{Tr}_p}N,
\qquad\text{(G7)}
$$

where the first arrow is the projection formula. These maps exist for
unbounded complexes by
[Stacks, Tag 0F0C](https://stacks.math.columbia.edu/tag/0F0C) and
[Stacks, Tag 0GL5](https://stacks.math.columbia.edu/tag/0GL5).

*First triangle identity.* We show that
$\varepsilon_{Rp_*M}\circ Rp_*(\eta_M)=1_{Rp_*M}$. Using composition of direct
images, $pp_1=pp_2$, proper base change and the projection formula, this
composite equals

$$
\begin{aligned}
Rp_*M
&=R(pp_1)_*\Delta_*M\\
&\longrightarrow R(pp_1)_*p_1^*M(1)[2]\\
&\xrightarrow{\ \sim\ }
      Rp_*\bigl(M\otimes_\Lambda^{\mathbf L}Rp_{1*}\Lambda_{\mathbf P^1_S\times_S\mathbf P^1_S}(1)[2]\bigr)\\
&\xrightarrow{Rp_*(1_M\otimes \operatorname{Tr}_{p_1})}Rp_*M .
\end{aligned}
\qquad\text{(G8)}
$$

Here the first arrow is $Rp_*$ of the first arrow of (G6), with $R(pp_2)_*$
rewritten as $R(pp_1)_*$. The middle isomorphism is the projection formula for
$p_1$; it replaces the proper base change isomorphism of (G6), after $Rp_*$,
followed by the projection formula isomorphism of (G7). The last arrow replaces
$1\otimes\operatorname{Tr}_p$ in (G7) by $\operatorname{Tr}_{p_1}$, the base
change of $\operatorname{Tr}_p$ along $p$ ([sk-lem-geo-p1-cohomology]). In
this form, the trace is applied to $Rp_{1*}\delta$, that is, to the factor
$\Delta_*\Lambda$, and $M$ only appears as a coefficient.

This rewriting is an equality of maps because the projection formula
isomorphism is compatible with proper base change. To see this, recall that
the proper base change map is the adjoint transpose of the counit of
$g^*\dashv Rg_*$ for the relevant pullback $g$, and that the projection map is
the adjoint transpose of the same counit tensored with the identity. Since the
counit of a composite adjunction is the composite of the counits, the two
routes from $R(pp_2)_*p_1^*M=R(pp_1)_*p_1^*M$ to
$Rp_*M\otimes Rp_*\Lambda(1)[2]$ have the same adjoint transpose, as in the
pasting lemma [sk-lem-pbc-exchange-pasting]. On the route through (G8) we
identify $Rp_{1*}\Lambda=p^*Rp_*\Lambda$ by proper base change and then use the
projection formula for $p$. By naturality of the projection formula in its
second variable, the first arrow of (G8) is then $1_M\otimes Rp_{1*}\delta$
under the projection identification, and the composite is
$Rp_*(1_M\otimes s_1)=1_{Rp_*M}$ by the claim.

*Second triangle identity.* We take $M=p^*N(1)[2]$ in (G6). Then $p_1^*M$ and
$p_2^*M$ are both $(pp_1)^*N(1)[2]=(pp_2)^*N(1)[2]$, since $N$ and the Tate
twist are pulled back from $S$. By the projection formula, we may therefore
move this common factor outside $Rp_{2*}$, so that $\eta_{p^*N(1)[2]}$ becomes
$1\otimes Rp_{2*}\delta$. By the base change compatibility of (G3),
$p^*(\varepsilon_N)(1)[2]$ becomes $1\otimes\operatorname{Tr}_{p_2}$, applied
to the target of $Rp_{2*}\delta$. This gives

$$
p^*(\varepsilon_N)(1)[2]\circ\eta_{p^*N(1)[2]}
     =1_{p^*N(1)[2]}\otimes(\operatorname{Tr}_{p_2}\circ Rp_{2*}\delta)
     =1_{p^*N(1)[2]}\otimes s_2=1_{p^*N(1)[2]}. \qquad\text{(G9)}
$$

All shifts moved in (G8) and (G9) are even, so no Koszul signs appear.

Finally, the unit is constructed from $\delta$ and proper base change, and the
counit from (G3) and the projection formula. Since all of these are compatible
with base change and change of coefficients, so are $\eta$ and $\varepsilon$,
and by the comparison the same holds on the pro-étale categories of (G4).
