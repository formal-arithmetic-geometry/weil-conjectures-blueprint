+++
kind  = "proof"
of    = "thm-trf-fixed-point-base-change"
+++
The first identification is the functoriality of the derived pullback
along the equality $c_2i_F=d$ of
[prop-trf-fixed-square-cartesian]:

$$
Li_F^*Lc_2^*K=L(c_2i_F)^*K=Ld^*K.
$$

The second is the compact-support exchange
$Lg^*Rf_!\xrightarrow{\sim}Rf'_!Lg'^*$ of
[def-exchange-projection] (and of the six-operations package
[prop-functor-package], item (4)) applied to the Cartesian fixed
square of [prop-trf-fixed-square-cartesian] with $f=c$,
$g=\Delta_X$, $f'=d$, $g'=i_F$. The right-adjoint form is
obtained by taking right adjoints of the two sides and using the
compatibility of the exchange with the units and counits of the
adjunctions of [def-trf-admissibility]: the right adjoint of
$L\Delta_X^*Rc_!$ is $Rc^!R\Delta_{X*}$, and that of $Rd_!Li_F^*$
is $Ri_{F*}Rd^!$. (The derived pullbacks of
[def-weil-derived-pullback-tensor-hom] used in the first
identification are the ones defined by exact inverse image followed by
the flat extension along the constant coefficient sheaf; no analogue of
these statements for the single exceptional leg $c_1$ is asserted
(the naive version $Li_F^*Rc_1^!K\cong Rd^!K$ is false).
