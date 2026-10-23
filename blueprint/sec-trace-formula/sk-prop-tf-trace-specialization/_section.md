+++
id = "sk-prop-tf-trace-specialization"
kind = "proposition"
title = "Specialization of the trace class"
order = 3600
uses = ["sk-prop-tf-nearby-duality-foundation", "sk-lem-tf-nearby-mate-coherences", "sk-d-trace-class", "sk-thm-sf-kunneth-verdier", "sk-prop-tf-nearby-external-kunneth"]
tags = ["sketch"]
+++
Let $S$ be the strictly henselian trait and $A$ the coefficient ring of
[sk-prop-tf-nearby-duality-foundation], with special point $s$ and generic point $\eta$,
and write $S_X=R\Psi_{X/S}$ for nearby cycles. For a morphism $f$ of separated
finite-type $S$-schemes, $\alpha_f:f_s^*S\to Sf_\eta^*$ and
$\beta_f:Sf_\eta^!\to f_s^!S$ are the pullback and exceptional exchanges,
$\sigma_X:A_{X_s}\to S_XA_{X_\eta}$ is the specialization unit and
$\theta_X:S_X\omega_{X_\eta}\to\omega_{X_s}$ the dualizing map, as in
[sk-lem-tf-nearby-mate-coherences]; $\operatorname{Tr}_c(u):A_F\to\omega_F$ is the trace
class of [sk-d-trace-class].

Let $c=(c_1,c_2):C\to X\times_SX$ be a correspondence of separated
finite-type schemes over the trait $S$, and let $F=F_c$ be its
fixed scheme, with $r:F\hookrightarrow C$ and $d:F\to X$.
For $K\in\Dctf(X_\eta,A)$ and a morphism
$u:c_{2\eta}^*K\to c_{1\eta}^!K$, put $K'=S_XK$ and
let $u_s$ be the composite

$$
 u_s:c_{2s}^*K'\xrightarrow{\alpha_{c_2}}S_Cc_{2\eta}^*K
       \xrightarrow{S_Cu}S_Cc_{1\eta}^!K
       \xrightarrow{\beta_{c_1}}c_{1s}^!K'.
$$

For a dualizing section $z:A_{F_\eta}\to\omega_{F_\eta}$, its
specialization is

$$
 \operatorname{sp}_F(z)=\theta_F S_F(z)\sigma_F:
 A_{F_s}\longrightarrow\omega_{F_s}.
$$

Then

$$
 \operatorname{Tr}_{c_s}(u_s)
     =\operatorname{sp}_F\bigl(\operatorname{Tr}_{c_\eta}(u)\bigr).
$$

The legs $c_1,c_2$ may be nonproper. In particular the proposition applies
to the deformation of a correspondence to the normal cone, whose
generic fibre is the original correspondence.
