+++
kind = "proof"
of = "proposition-adjunction-projective-line"
order = 554
uses = ["proposition-forgetting-supports-composition", "lemma-class-diagonal-projective-line"]
+++
The projection formula and proper base change reduce each of the two
triangle identities to the identity $s_i=1$ of
Lemma [lemma-class-diagonal-projective-line], tensored with the
identity of a coefficient complex.

*First triangle identity.* This is the equation
$\varepsilon_{Rp_*M}\circ Rp_*(\eta_M)=1_{Rp_*M}$. Using composition of
direct images, $pp_1=pp_2$, proper base change and the projection
formula, this composite equals

$$
\begin{split}
Rp_*M
&=R(pp_1)_*\Delta_*M\\
&\longrightarrow R(pp_1)_*p_1^*M(1)[2]\\
&\xrightarrow{\ \sim\ }
Rp_*\bigl(M\otimes_A^{\mathbf L}
Rp_{1*}A_{\mathbf P^1_S\times_S\mathbf P^1_S}(1)[2]\bigr)\\
&\xrightarrow{Rp_*(1_M\otimes \operatorname{Tr}_{p_1})}Rp_*M .
\end{split}
\tag{6.8}
$$

Here the first arrow is $Rp_*$ of the first arrow of (6.5), with
$R(pp_2)_*$ rewritten as $R(pp_1)_*$. The middle isomorphism is the
projection formula for $p_1$. It replaces the proper base change
isomorphism of (6.5), after $Rp_*$, followed by the projection formula
isomorphism of (6.6). The last arrow replaces $1\otimes\operatorname{Tr}_p$
in (6.6) by $\operatorname{Tr}_{p_1}$, the base change of
$\operatorname{Tr}_p$ along $p$ (Lemma [lemma-cohomology-projective-line-trace]).
In this form, the trace is applied to $Rp_{1*}\delta$, that is, to the
factor $\Delta_*A$, and $M$ only appears as a coefficient.

This rewriting is an equality of maps because the projection formula
isomorphism is compatible with proper base change. To see this, recall
that the proper base change map is the adjoint transpose of the counit of
$g^*\dashv Rg_*$ for the relevant pullback $g$. The projection map is the adjoint transpose of the same counit tensored with the identity, and the counit of a composite adjunction is the composite of the counits.
Therefore the two routes from $R(pp_2)_*p_1^*M=R(pp_1)_*p_1^*M$ to
$Rp_*M\otimes Rp_*A(1)[2]$ have the same adjoint transpose, as in
the pasting Lemma [lemma-identity-pasting].

On the route through (6.8) we identify
$Rp_{1*}A=p^*Rp_*A$ by proper base change and then use the
projection formula for $p$. By naturality of the projection formula in its
second variable, the first arrow of (6.8) is then
$1_M\otimes Rp_{1*}\delta$ under the projection identification. The
composite is therefore $Rp_*(1_M\otimes s_1)$, which is $1_{Rp_*M}$ by
Lemma [lemma-class-diagonal-projective-line].

*Second triangle identity.* Here the roles of the two projections
are exchanged: we must show that
$p^*(\varepsilon_N)(1)[2]\circ\eta_{p^*N(1)[2]}$ is the identity.
Take $M=p^*N(1)[2]$ in (6.5). Since $N$ and the Tate twist are
pulled back from $S$, both $p_1^*M$ and $p_2^*M$ are
$(pp_1)^*N(1)[2]=(pp_2)^*N(1)[2]$. The projection formula moves this common
factor outside $Rp_{2*}$, and $\eta_{p^*N(1)[2]}$ becomes
$1\otimes Rp_{2*}\delta$. By the base change compatibility of (6.3),
$p^*(\varepsilon_N)(1)[2]$ becomes $1\otimes\operatorname{Tr}_{p_2}$,
applied to the target of $Rp_{2*}\delta$. We obtain

$$
p^*(\varepsilon_N)(1)[2]\circ\eta_{p^*N(1)[2]}
=1_{p^*N(1)[2]}\otimes
(\operatorname{Tr}_{p_2}\circ Rp_{2*}\delta)
=1_{p^*N(1)[2]}\otimes s_2=1_{p^*N(1)[2]}.
\tag{6.9}
$$

All shifts moved in (6.8) and (6.9) are even, so no Koszul signs appear.

The unit is constructed from $\delta$ and proper base change, and
the counit from (6.3) and the projection formula. All of these ingredients are compatible with base change and change of coefficients, and hence so
are $\eta$ and $\varepsilon$. Transported by $\nu^*$, the same then holds for the corresponding adjunction
on the pro-étale categories.
