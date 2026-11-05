+++
kind = "proof"
of = "corollary-point-counting-zeta-function--4"
order = 1040008
uses = ["theorem-trace-formula-euler-product--2", "corollary-point-counting-zeta-function--6"]
+++
A closed point of degree $e$ contributes exactly $e$ points over $\mathbf F_{q^m}$ when $e\mid m$, and none otherwise. Thus $\#X_0(\mathbf F_{q^m})=\sum_{e\mid m}eN_e$, where $N_e$ counts degree-$e$ closed points. Substitute this into the defining exponential for $Z$ and use $-\log(1-T^e)=\sum_{r\ge1}T^{er}/r$. Exponentiation gives the Euler product; every coefficient involves only finitely many closed points.

*Source:* the proof of Corollary [corollary-point-counting-zeta-function].
