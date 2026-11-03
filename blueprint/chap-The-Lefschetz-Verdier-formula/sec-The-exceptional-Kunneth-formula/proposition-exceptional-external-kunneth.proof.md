+++
kind = "proof"
of = "proposition-exceptional-external-kunneth"
order = 902
+++
Both sides of $\alpha$ are exact in each variable, so by dévissage it is
enough to check $\alpha$ on generators.
For constant coefficients we compute $f_i^!$ by
Theorem [theorem-smooth-purity-all-admissible-coefficients] for smooth maps and by localization, and check $\alpha$ directly. General
coefficients are built from extensions by zero $j_!F$ of lisse sheaves.
Since $f^!$ does not commute with $j_!$, we replace $j_!$ by
$Rj_*$, which does. The difference has smaller support, and we treat it
by induction. For the classical statements see
[sga5, III, (1.6.4), (1.7.3), Proposition 1.7.4 and (3.1.1)].

*Constant and lisse coefficients.*
First let the coefficients be constant. For smooth $f_i$ of relative
dimensions $d_i$, Theorem [theorem-smooth-purity-all-admissible-coefficients] identifies $f_i^!L_i$
with $f_i^*L_i(d_i)[2d_i]$, and $(f_1\times f_2)^!$ with
$(f_1\times f_2)^*(d_1+d_2)[2d_1+2d_2]$, so both sides of $\alpha$ become
the same twisted pullback. That $\alpha$ is this identification follows from
the compatibility of the trace map (Definition [definition-trace-map])
with products. Indeed, $\alpha$ is defined through the counits, and for
a smooth map the trace map is the counit composed with $\gamma_f$.

For closed immersions we use the localization triangle and the case of
ordinary external Künneth where one factor is the identity, applied
to the complementary open immersions. Every map factors locally as a
closed immersion followed by a smooth projection of affine spaces. Since
$\alpha$ is compatible with composition of morphisms and with
restriction to open subschemes, Zariski localization gives the constant case for general
maps. Lisse finite flat coefficients become
constant with finite projective values on an étale cover. Descent
therefore gives the lisse case, and then the case of bounded perfect lisse
models. In each of these steps the isomorphism we obtain is $\alpha$ itself.
For smooth maps this holds because $\gamma_f$ identifies the counit with the
trace map. For localization and descent it holds because $\alpha$ is natural
and compatible with restriction.

*General coefficients.*
A constructible complex is lisse on a dense open, and the rest has
smaller support. We therefore argue by induction on the sum of the dimensions of the supports
of $L_1,L_2$. Pushforward along closed immersions is compatible with
$\alpha$ by proper base change and the exceptional exchange of
Corollary [corollary-verdier-exchange-formulas]. Hence we may first assume that the
support is the entire base. As both sides of $\alpha$ are exact in each
variable, a finite constructible stratification,
bounded flat models and two-out-of-three reduce us to generators
$j_{i!}F_i$ for dense open $j_i:U_i\hookrightarrow Y_i$, with $F_i$
a lisse sheaf with finite projective stalks
(Lemma [lemma-flat-models-generators]).

Since $f_i^!$ does not commute with $j_{i!}$ in
general, we pass through $Rj_{i*}$. Let $j'_i$ and $f_{i,U}$ be
the base changes of $j_i$ and $f_i$. The exceptional exchange
$f_i^!Rj_{i*}\simeq Rj'_{i*}f_{i,U}^!$ is the mate, under the right
adjoints, of base change for $Rf_{i!}$ along the open immersion. Hence
it is compatible with the counits used to define $\alpha$. By this
exchange and the ordinary external Künneth formula, the comparison on
$(Rj_{1*}F_1,Rj_{2*}F_2)$ is the pushforward of the lisse comparison.
Let $z_i:Z_i\hookrightarrow Y_i$ be the closed complement of $U_i$. In
the triangles

$$
j_{i!}F_i\longrightarrow Rj_{i*}F_i\longrightarrow
z_{i*}z_i^*Rj_{i*}F_i\xrightarrow{+1},
$$

the third term is still constructible of finite Tor amplitude by
Proposition [proposition-six-operations-dctf], and its support has smaller dimension.
Since $\alpha$ is natural, it maps the corresponding
triangles to each other in each variable. By induction and two-out-of-three, first
in one variable and then in the other, we obtain $\alpha$ for
$(j_{1!}F_1,j_{2!}F_2)$.
