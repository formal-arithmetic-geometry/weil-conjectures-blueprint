+++
kind = "proof"
of = "sk-prop-geo-p1-adjunction"
uses = ["sk-lem-geo-cartier", "sk-lem-geo-p1-cohomology", "sk-prop-pe-unbounded-classical"]
+++
We calculate on $D((\mathbf P^1_S)_{\mathrm{ét}},\Lambda)$ and
$D(S_{\mathrm{ét}},\Lambda)$, using the classical equivalence of
[sk-prop-pe-unbounded-classical]; until the last paragraph, $Rp_*$, $p^*$,
$Rp_{a*}$, $p_a^*$, $\Delta_*$ and $\otimes^{\mathbf L}$ are the functors
between these étale derived categories and that of
$\mathbf P^1_S\times_S\mathbf P^1_S$. Transporting the resulting unit and
counit gives (G4) on the stated pro-étale categories. The direct-image
comparison identifies the canonical exchange and projection maps used in this
transport.

The counit will be the trace (G3), and the unit will be built from the cycle
class of the diagonal. The triangle identities then reduce to a single fact:
integrating the class of the diagonal along either factor gives $1$.

Let $p_1,p_2:\mathbf P^1_S\times_S\mathbf P^1_S\to\mathbf P^1_S$ be the
projections and
$\Delta:\mathbf P^1_S\hookrightarrow\mathbf P^1_S\times_S\mathbf P^1_S$ the
diagonal. It is cut out by $x_0y_1-x_1y_0$, so it is a relative effective
Cartier divisor, and it stays one after every base change.
[sk-lem-geo-cartier] gives its cycle class

$$
\delta:\Delta_*\Lambda_{\mathbf P^1_S}\longrightarrow
  \Lambda_{\mathbf P^1_S\times_S\mathbf P^1_S}(1)[2]
  \quad\text{in }D((\mathbf P^1_S\times_S\mathbf P^1_S)_{\mathrm{ét}},\Lambda).
$$

For $a=1,2$, the projection $p_a$ is a projective line over the other factor,
with trace $\operatorname{Tr}_{p_a}$ given by (G3) of
[sk-lem-geo-p1-cohomology]. Integrating $\delta$ along $p_a$ gives an
endomorphism in $D((\mathbf P^1_S)_{\mathrm{ét}},\Lambda)$

$$
s_a:\Lambda_{\mathbf P^1_S}=Rp_{a*}\Delta_*\Lambda_{\mathbf P^1_S}
      \xrightarrow{Rp_{a*}\delta}
      Rp_{a*}\Lambda_{\mathbf P^1_S\times_S\mathbf P^1_S}(1)[2]
      \xrightarrow{\operatorname{Tr}_{p_a}}\Lambda_{\mathbf P^1_S}. \qquad\text{(G5)}
$$

*Claim: $s_1=s_2=1$.* Both sides are endomorphisms of a sheaf placed in degree
zero, and

$$
\Hom_{D((\mathbf P^1_S)_{\mathrm{ét}},\Lambda)}(\Lambda_{\mathbf P^1_S},\Lambda_{\mathbf P^1_S})
  =\Hom_{\Mod((\mathbf P^1_S)_{\mathrm{ét}},\Lambda)}(\Lambda_{\mathbf P^1_S},\Lambda_{\mathbf P^1_S}),
$$

so $s_a$ is a morphism of sheaves and is determined by its geometric stalks.
By proper base change, the stalk of (G5) at a geometric point $\bar x$ is the
trace of the cycle class of the single point cut out by the diagonal in the
fibre $\mathbf P^1_{\bar x}$. The line bundle of that point has degree one, so
by (G2) and (G3) its trace is $1$.

*The unit and counit.* For $M\in D((\mathbf P^1_S)_{\mathrm{ét}},\Lambda)$
define the morphism (G6)

$$
\eta_M:M=Rp_{2*}\Delta_*M\longrightarrow Rp_{2*}\bigl(p_1^*M(1)[2]\bigr)
  \xrightarrow{\ \sim\ }p^*Rp_*M(1)[2].
$$

Here the first arrow is $Rp_{2*}$ applied to $\delta\otimes p_1^*M$, using the
projection formula $\Delta_*M=\Delta_*\Lambda\otimes^{\mathbf L}p_1^*M$ in
$D((\mathbf P^1_S\times_S\mathbf P^1_S)_{\mathrm{ét}},\Lambda)$, and the second
is the proper base-change isomorphism $p^*Rp_*\simeq Rp_{2*}p_1^*$ of functors
$D((\mathbf P^1_S)_{\mathrm{ét}},\Lambda)\to D((\mathbf P^1_S)_{\mathrm{ét}},\Lambda)$.
For $N\in D(S_{\mathrm{ét}},\Lambda)$ define the morphism (G7)

$$
\epsilon_N:Rp_*\bigl(p^*N(1)[2]\bigr)
  \xrightarrow{\ \sim\ }N\otimes_\Lambda^{\mathbf L}Rp_*\Lambda_{\mathbf P^1_S}(1)[2]
  \xrightarrow{1\otimes \operatorname{Tr}_p}N,
$$

the first arrow being the projection formula. These maps exist for unbounded
complexes by Stacks, Tags [0F0C](https://stacks.math.columbia.edu/tag/0F0C)
and [0GL5](https://stacks.math.columbia.edu/tag/0GL5).

*First triangle identity.* We show
$\epsilon_{Rp_*M}\circ Rp_*(\eta_M)=1_{Rp_*M}$. Using composition of direct
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

In words: the unit (G6) integrates over the first coordinate with the second
fixed, and the counit (G7), after $Rp_*$, integrates over the second.
Rewriting $R(pp_2)_*$ as $R(pp_1)_*$ and applying the projection formula with
coefficient $M$ moves the integration into the kernel factor, where the trace
is $\operatorname{Tr}_{p_1}$, the base change of $\operatorname{Tr}_p$.

This rewriting is an equality of maps because of how the canonical maps are
defined: the proper base-change map is the adjoint transpose of the counit of
$g^*\dashv Rg_*$ for the relevant pullback $g$, and the projection map is the
adjoint transpose of tensoring with the same counit. Expanding these
definitions along either route uses this counit once in each coordinate, in
the same order once $pp_1=pp_2$ is used. Hence the first arrow of (G8) is
$1_M\otimes Rp_{1*}\delta$ under the projection identification, and the
composite is $Rp_*(1_M\otimes s_1)=1_{Rp_*M}$ by the claim.

*Second triangle identity.* Take $M=p^*N(1)[2]$ in (G6). Then $p_1^*M$ and
$p_2^*M$ are both $(pp_1)^*N(1)[2]=(pp_2)^*N(1)[2]$, since $N$ and the Tate
twist are pulled back from $S$. The projection formula therefore takes this
common factor outside $Rp_{2*}$, and applying $p^*(\epsilon_N)(1)[2]$
contracts the remaining kernel by $\operatorname{Tr}_{p_2}$:

$$
p^*(\epsilon_N)(1)[2]\circ\eta_{p^*N(1)[2]}
     =1_{p^*N(1)[2]}\otimes(\operatorname{Tr}_{p_2}\circ Rp_{2*}\delta)
     =1_{p^*N(1)[2]}\otimes s_2=1_{p^*N(1)[2]}. \qquad\text{(G9)}
$$

All shifts moved in (G8) and (G9) are even, so no Koszul signs appear.

Finally, the unit is built from $\delta$ and proper base change, and the counit
from (G3) and the projection formula. All of these are compatible with base
change and change of coefficients, hence so are $\eta$ and $\epsilon$, as
natural transformations of functors on $D((\mathbf P^1_S)_{\mathrm{ét}},\Lambda)$
and $D(S_{\mathrm{ét}},\Lambda)$; the comparison transports this to the
pro-étale categories of (G4).

*The complement.* The diagonal integrals are the claim $s_1=s_2=1$ above.
For the restriction to $\Dctf$: $Rp_*$ preserves constructible complexes of
finite Tor amplitude because $p$ is proper, and $p^*(-)(1)[2]$ preserves them,
being an inverse image followed by a twist by an invertible sheaf and a shift.
Since $\Dctf$ is a full subcategory on both sides, the Hom groups computing the
adjunction are unchanged, so (G4) restricts with the same unit and counit.
