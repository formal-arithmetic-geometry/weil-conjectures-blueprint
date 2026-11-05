+++
id = "proposition-sp-unique-adjoint"
kind = "proposition"
title = "Uniqueness of the right adjoint of $Rf_!$"
name_showing = false
order = 762
lean = ["CategoryTheory.Adjunction.rightAdjointUniq", "CategoryTheory.Adjunction.rightAdjointUniq_hom_app_counit"]
uses = ["theorem-existence-exceptional-inverse-image", "theorem-exceptional-inverse-image--18"]
+++
Let $\Lambda$ be an admissible coefficient ring and let $J$ be a right adjoint of
$Rf_!:D^b_{\mathrm{ctf}}(X,\Lambda)\to D^b_{\mathrm{ctf}}(Y,\Lambda)$ with counit $\varepsilon^J$.
There is a unique natural isomorphism $\rho:f^!\xrightarrow{\sim}J$ with
$\varepsilon^J(K)\circ Rf_!(\rho(K))=\varepsilon_f(K)$.
