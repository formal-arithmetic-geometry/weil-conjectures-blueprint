+++
kind = "proof"
of = "det-nearby-exceptional-tensor"
uses = ["det-nearby-exchange-maps"]
+++
(1) Check the identity before restricting by $i_W^*$, on the total families, where $\nu_f$ is the
restriction of the map $Rf_!Rj_{V*}\to Rj_{W*}Rf_{\eta!}$ whose $j_W^*$-adjoint is
$j_W^*Rf_!Rj_{V*}\simeq Rf_{\eta!}j_V^*Rj_{V*}\to Rf_{\eta!}$, induced by the counit of $j_V$. Take
$j_W^*$-adjoints of both sides. Both adjoints are the counit $j_V^*Rj_{V*}\to1$ tensored with the
identity, followed by the generic projection formula for $f_\eta$. Hence the two maps agree.

(2) Take $Rf_{s!}$-adjoints of both sides. By the definition of $\beta_f$ as the exceptional
adjoint of $S_W\varepsilon_{f_\eta}\circ\nu_f$, and by (1), after the projection formula both
adjoints become the common composite

$$
\begin{aligned}
Rf_{s!}S_Vf_\eta^!M\dt S_WN
&\xrightarrow{\nu_f\otimes1}S_W(Rf_{\eta!}f_\eta^!M)\dt S_WN\\
&\xrightarrow{\mu_W}S_W(Rf_{\eta!}f_\eta^!M\dt N)
\xrightarrow{S_W(\varepsilon_{f_\eta}\otimes1)}S_W(M\dt N).
\end{aligned}
$$

On the right side this uses that the adjoint of $t_{f_s}$ is $\varepsilon_{f_s}\otimes1$ after the
projection formula; on the left side it uses the same description of $t_{f_\eta}$ and naturality of
$\nu_f$ and $\mu_W$.

(3) Take exceptional adjoints. The adjoint of $\beta_{gf}$ is
$S_Z\varepsilon_{(gf)_\eta}\circ\nu_{gf}$. By the composition law for $\nu$ in
[det-nearby-exchange-maps] and the composition of counits
$\varepsilon_{gf}=\varepsilon_g\,Rg_!\varepsilon_f$, it equals the adjoint of
$f_s^!\beta_g\ \beta_f(g_\eta^!)$. The identity for $\theta$ is the case $g=a_W$, $M=A$, using
$a_V=a_Wf$ and $f_\eta^!\omega_{W_\eta}=\omega_{V_\eta}$.
