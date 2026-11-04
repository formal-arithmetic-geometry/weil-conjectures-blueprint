+++
kind = "proof"
of = "sk-prop-tf-exceptional-external-kunneth"
uses = ["sk-thm-purity-transport", "sk-def-sp-trace", "sk-thm-sf-verdier-exchange", "sk-thm-sf-ctf-stability"]
+++
For constant coefficients $f_i^!$ is computed by
Theorem [sk-thm-purity-transport] for smooth maps and by localization, and $\alpha$ can be checked directly. General
coefficients are built from extensions by zero $j_!F$ of lisse sheaves,
but $f^!$ does not commute with $j_!$. The point is to replace $j_!$ by
$Rj_*$, which does commute with $f^!$, and to treat the difference,
which has smaller support, by induction. For the classical statements see
[sga5, III, (1.6.4), (1.7.3), Proposition 1.7.4 and (3.1.1)].

*Constant and lisse coefficients.*
First let the coefficients be constant. For smooth maps we use Theorem [sk-thm-purity-transport]
and the compatibility of the trace map (Definition [sk-def-sp-trace]) with products. For closed
immersions we use the localization triangle and the case of
ordinary external Künneth where one factor is the identity, applied
to the complementary open immersions. Since every map factors locally as a
closed immersion followed by a smooth projection of affine spaces, and
$\alpha$ is compatible with composition of morphisms and with
restriction to open subschemes, we obtain the constant case for general
maps by Zariski localization. Lisse finite flat coefficients become
constant with finite projective values on an étale cover, and by
descent we obtain the lisse case and then the case of bounded perfect lisse models. In each of
these steps the isomorphism obtained is $\alpha$ itself: for smooth maps
because $\gamma_f$ identifies the counit with the trace map, and for
localization and descent because $\alpha$ is natural and compatible
with restriction.

*General coefficients.*
We argue by induction on the sum of the dimensions of the supports
of $L_1,L_2$. Pushforward along closed immersions is compatible with
$\alpha$ by proper base change and the exceptional exchange of
Corollary [sk-thm-sf-verdier-exchange], so we may first assume that the
support is the entire base. Both sides of $\alpha$ are exact in each
variable, so a finite constructible stratification and
bounded flat models reduce us, by two-out-of-three, to generators
$j_{i!}F_i$ for dense open $j_i:U_i\hookrightarrow Y_i$, with $F_i$
lisse and perfect. Since $f_i^!$ does not commute with $j_{i!}$ in
general, we pass through $Rj_{i*}$. The exceptional exchange
$f_i^!Rj_{i*}\simeq Rj'_{i*}f_{i,U}^!$, where $j'_i$ and $f_{i,U}$ are
the base changes of $j_i$ and $f_i$, is the mate, under the right
adjoints, of base change for $Rf_{i!}$ along the open immersion, and
hence it is compatible with the counits used to define $\alpha$. By this
exchange and the ordinary external Künneth formula, the comparison on
$(Rj_{1*}F_1,Rj_{2*}F_2)$ is the pushforward of the lisse comparison.
Let $z_i:Z_i\hookrightarrow Y_i$ be the closed complement of $U_i$. In
the triangles

$$
j_{i!}F_i\longrightarrow Rj_{i*}F_i\longrightarrow
z_{i*}z_i^*Rj_{i*}F_i\xrightarrow{+1},
$$

the third term is still constructible of finite Tor amplitude by
Proposition [sk-thm-sf-ctf-stability], and its support has smaller dimension.
Since $\alpha$ is natural, it maps the corresponding
triangles to each other in each variable. By induction and two-out-of-three, first
in one variable and then in the other, we obtain $\alpha$ for
$(j_{1!}F_1,j_{2!}F_2)$.
