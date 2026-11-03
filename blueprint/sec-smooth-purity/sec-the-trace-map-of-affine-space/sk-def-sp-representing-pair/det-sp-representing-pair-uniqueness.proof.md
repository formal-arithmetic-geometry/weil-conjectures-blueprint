+++
kind = "proof"
of = "det-sp-representing-pair-uniqueness"
uses = ["det-sf-existence-brown", "sk-lem-sp-finite-existence"]
+++
*(1)* Apply the defining bijection of $(H',\varepsilon')$ to $M=H\in\Dctf$: there
is a unique $\phi:H\to H'$ with $\varepsilon'\circ Rf_!(\phi)=\varepsilon$.
Symmetrically there is a unique $\psi:H'\to H$ with
$\varepsilon\circ Rf_!(\psi)=\varepsilon'$. Then
$\varepsilon\circ Rf_!(\psi\phi)=\varepsilon'\circ Rf_!(\phi)=\varepsilon=\varepsilon\circ Rf_!(\mathrm{id}_H)$,
and injectivity of the bijection for $(H,\varepsilon)$ at $M=H$ gives
$\psi\phi=\mathrm{id}_H$; likewise $\phi\psi=\mathrm{id}_{H'}$.

*(2)* For $M\in\Dctf(X,\Lambda_n)\subset\Loc(\Dctf(X,\Lambda_n))$ the adjunction
bijection $\Hom(M,f^!K)\to\Hom(Rf_!M,K)$ of [det-sf-existence-brown] is
$b\mapsto\varepsilon_K\circ Rf_!(b)$ (the standard expression of an adjunction
through its counit). So $(f^!K,\varepsilon_K)$ is a representing pair. That
$f^!K$ lies in $\Dctf(X,\Lambda_n)$ is the restriction theorem for $f^!$ (for
smooth $f$ it also follows from the chart computation of
[sk-lem-sp-finite-existence]). The last assertion is (1) applied to
$(H,\varepsilon)$ and $(f^!K,\varepsilon_K)$.
