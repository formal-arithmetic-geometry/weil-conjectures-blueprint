+++
kind = "proof"
of = "sk-thm-curve-package"
order = 1
uses = ["sk-prop-sf-comparison", "sk-thm-br", "sk-thm-curveestimate", "sk-prop-curve-affine-kummer", "sk-prop-curve-artin-schreier", "sk-lem-curve-affine-artin-schreier", "sk-lem-curve-finite-support", "sk-lem-curve-normalization", "sk-lem-curve-dense-open", "sk-lem-curve-sylow-trace"]
+++
The proof is in Appendix [sec-curve-estimates]. For a smooth proper connected curve and $n$
invertible in $k$, one computes $H^q(C,\mu_n)$ with the Kummer
sequence and the Jacobian (Appendix [sec-picard-framework]). For $p$-primary
coefficients one uses the Artin–Schreier sequence instead. The case of
general torsion sheaves is reduced to these cases by normalization, removal of
finitely many points and a finite étale cover of degree prime to the
torsion order.
