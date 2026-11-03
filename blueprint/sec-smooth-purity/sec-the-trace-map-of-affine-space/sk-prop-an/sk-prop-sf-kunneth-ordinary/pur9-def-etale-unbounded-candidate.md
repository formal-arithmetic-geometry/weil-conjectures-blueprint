+++
id = "pur9-def-etale-unbounded-candidate"
kind = "definition"
title = "Unbounded étale compactification candidate"
order = 3051
uses = ["pur7710-def-unbounded-etale-push", "sk-thm-sf-comp-composition"]
+++
For a separated morphism of finite type $f:X\to Y$ of $k$-schemes of finite type with chosen compactification $c_f=(j,p)$, put

$$
Rf^{\mathrm{un}}_{!,\Et,\mathcal O_E/\pi_E^n}:=Rp_{*,\Et,\mathcal O_E/\pi_E^n}\circ\mathrm D(j_{!,\Et,\mathcal O_E/\pi_E^n}):D(X_{\Et},\mathcal O_E/\pi_E^n)\longrightarrow D(Y_{\Et},\mathcal O_E/\pi_E^n),
$$

with the unbounded direct image of Definition [pur7710-def-unbounded-etale-push] and the exact extension by zero of Lemma “Exactness of étale extension by zero” (`pur456-pbc-open-exact`, in [sk-thm-sf-comp-composition]). By Definition [pur7710-def-unbounded-etale-push], its restriction to $D^+(X_{\Et},\mathcal O_E/\pi_E^n)$ is identified with $Rf_{!,\Et,\mathcal O_E/\pi_E^n}$ of Definition “Finite-coefficient étale compact-support direct image” (`pur456-pbc-lower-shriek`, in [sk-thm-sf-comp-composition]).
