+++
id = "proposition-sp-unique-adjoint"
kind = "proposition"
title = "Uniqueness of the right adjoint of $Rf_!$"
name_showing = false
order = 763
lean = ["CategoryTheory.Adjunction.rightAdjointUniq_hom_counit"]
+++
Let $\Lambda$ be an admissible coefficient ring and let $J$ be a right adjoint of
$\href{@proposition-construction-independence-rf-shriek}{Rf_!}:\href{@definition-constructible-sheaves}{D^b_{\mathrm{ctf}}(X,\Lambda)}\to \href{@definition-constructible-sheaves}{D^b_{\mathrm{ctf}}(Y,\Lambda)}$ with counit $\varepsilon^J$.
There is a unique natural isomorphism $\rho:\href{@theorem-existence-exceptional-inverse-image}{f^!}\xrightarrow{\sim}J$ with
$\varepsilon^J(K)\circ \href{@proposition-construction-independence-rf-shriek}{Rf_!(\rho(K))}=\varepsilon_f(K)$.
