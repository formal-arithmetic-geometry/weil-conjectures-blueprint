+++
kind = "proof"
of = "det-tf-transverse-corner-constant"
+++
*The surface.* The closed subscheme $Y_S$ of the strictly local scheme
$S$ is strictly local, so $R\Gamma(S,\mathbf F_\ell)$ and
$R\Gamma(Y_S,\mathbf F_\ell(-1))$ are $\mathbf F_\ell$ and
$\mathbf F_\ell(-1)$ in degree zero. By transitivity of the smooth
dualizing complexes of $S$ and of the regular divisor $Y_S$
([thm-pur-finite-coefficient-smooth-purity]),
$i_{Y_S}^!\mathbf F_\ell=\mathbf F_\ell(-1)[-2]$. The localization
triangle

$$
 R\Gamma(Y_S,i_{Y_S}^!\mathbf F_\ell)\longrightarrow
 R\Gamma(S,\mathbf F_\ell)\longrightarrow
 R\Gamma(S-Y_S,\mathbf F_\ell)\xrightarrow{+1}
$$

therefore has first term $\mathbf F_\ell(-1)[-2]$ and second term
$\mathbf F_\ell$, and its long exact sequence gives
$H^0(S-Y_S,\mathbf F_\ell)=\mathbf F_\ell$,
$H^1(S-Y_S,\mathbf F_\ell)\simeq H^2_{Y_S}(S,\mathbf F_\ell)=\mathbf F_\ell(-1)$
and $H^q(S-Y_S,\mathbf F_\ell)=0$ for $q\geq2$.

*The punctured trait.* $X_S$ is a strictly henselian trait with
fraction field $K$, and $X_S-z=\operatorname{Spec}K$. It is the filtered
limit of the punctured affine curve neighbourhoods of $z$ in étale
neighbourhoods of $z$ on $X$, and cohomology commutes with this limit;
each of these curves has cohomological dimension at most one
([lem-sc-affine-cohomological-dimension]), so $H^q(X_S-z,\mathbf F_\ell)=0$
for $q\geq2$. It is connected, so $H^0=\mathbf F_\ell$. The Kummer
sequence ([def-sc-kummer-sequence]) gives
$H^1(X_S-z,\mu_\ell)=K^*/K^{*\ell}$. The units of the strictly henselian
trait are $\ell$-divisible, because the residue field is algebraically
closed of characteristic $\ne\ell$ and Hensel's lemma applies to
$T^\ell-u$. Hence the valuation induces
$K^*/K^{*\ell}\simeq\mathbf Z/\ell$, a uniformizer having residue one,
and after twisting $H^1(X_S-z,\mathbf F_\ell)\simeq\mathbf F_\ell(-1)$.

*The restriction.* In degree zero both sides are the constants of a
connected scheme, and restriction is the identity. In degree one we
compare after twisting by $\mu_\ell$. Let $t$ be a local equation of
$Y_S$; it is a unit on $S-Y_S$, and its Kummer class has residue one
along $Y_S$, so it generates $H^1(S-Y_S,\mu_\ell)\simeq\mathbf Z/\ell$.
Since $X_S$ and $Y_S$ meet transversely at $z$, the restriction of $t$
to $X_S$ is a uniformizer, whose Kummer class has residue one as well.
Thus restriction sends a generator to a generator, and is an
isomorphism in degree one. Both complexes vanish in the other degrees,
so the restriction map is an isomorphism.
