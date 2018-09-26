#!C:/Users/dell laptap/AppData/Local/Programs/Python/Python36/python.exe
print("Content-Type:text/html")
print("""""")
print("<!DOCTYPE html>")
print("<html lang='en'>")
print("<head>")
print("    <meta charset='utf-8'>")
print("    <meta http-equiv='X-UA-Compatible' content='IE=edge'>")
print("    <meta name='viewport' content='width=device-width, initial-scale=1'>")
print("    <meta name='description' content=''>")
print("    <meta name='author' content=''>")
print("    <link rel='icon' type='image/png' sizes='16x16' href='admin/assets/images/favicon.png'>")
print("    <title>STOCK PREDICTION</title>")
print("    <link href='admin/assets/plugins/bootstrap/css/bootstrap.min.css' rel='stylesheet'>")
print("    <link href='admin/main/css/style.css' rel='stylesheet'>")
print("    <link href='admin/main/css/colors/blue.css' id='theme' rel='stylesheet'>")
print("</head>")
print("<body class='fix-header card-no-border'>")
print("    <div id='main-wrapper'>")
print("        <header class='topbar'>")
print("            <nav class='navbar top-navbar navbar-expand-md navbar-light'>")
print("                <div class='navbar-header'>")
print("                    <a class='navbar-brand' href='index.html'>")
print("                            <img src='admin/logo1.png' alt='homepage' class='dark-logo' />")
print("                            <img src='admin/assets/images/logo-light-icon.png' alt='homepage' class='light-logo' />")
print("                        </b><span>")

print("                </div>")
print("                <div class='navbar-collapse'>")
print("                    <ul class='navbar-nav mr-auto mt-md-0'>")
print("                        <!-- This is  -->")
print("                        <li class='nav-item'> <a class='nav-link nav-toggler hidden-md-up text-muted waves-effect waves-dark' href='javascript:void(0)'><i class='mdi mdi-menu'></i></a> </li>")
print("                        <li class='nav-item m-l-10'> <a class='nav-link sidebartoggler hidden-sm-down text-muted waves-effect waves-dark' href='javascript:void(0)'><i class='ti-menu'></i></a> </li>")
print("                    </ul>")
print("                    <ul class='navbar-nav my-lg-0'>")

print("                        <li class='nav-item dropdown'>")
print("                            <a class='nav-link dropdown-toggle text-muted waves-effect waves-dark' href='#' data-toggle='dropdown' aria-haspopup='true' aria-expanded='false'><img src='admin/assets/images/users/1.jpg' alt='user' class='profile-pic' /></a>")
print("                            <div class='dropdown-menu dropdown-menu-right scale-up'>")
print("                                <ul class='dropdown-user'>")
print("                                    <li><a href='front.py'><i class='fa fa-power-off'></i> Logout</a></li>")
print("                                </ul>")
print("                            </div>")
print("                        </li>")
print("                    </ul>")
print("                </div>")
print("            </nav>")
print("        </header>")
print("        <aside class='left-sidebar'>")
print("            <div class='scroll-sidebar'>")
print("                <div class='user-profile'>")
print("                    <div class='profile-img'> <img src='admin/circle.png' alt='user' />")
print("                            <div class='notify setpos'> <span class='heartbit'></span> <span class='point'></span> </div>")
print("                    </div>")
print("                    <div class='profile-text'>")
print("                            <h5>Admin</h5>")
print("                              <a href='front.py' class='' data-toggle='tooltip' title='Logout'><i class='mdi mdi-power'></i></a>")
print("                    </div>")
print("                </div>")
print("<nav class='sidebar-nav'>")
print("                    <ul id='sidebarnav'>")
print("                         <li class='nav-devider'></li>")
print("<li><a class='has-arrow waves-effect waves-dark' href=data.py target=mw><i class='mdi mdi-bullseye'></i><span class='hide-menu'>Training Data</span></a></li>")
print("<li><a class='has-arrow waves-effect waves-dark' href=testdata.py target=mw><i class='mdi mdi-bullseye'></i><span class='hide-menu'>Test Data</span></a></li>")
print("<li><a class='has-arrow waves-effect waves-dark' href=CLosePrice_Turnover.py target=mw><i class='mdi mdi-bullseye'></i><span class='hide-menu'>ClosePrice VS Turnover(in Lakhs)</span></a></li>")
print("<li><a class='has-arrow waves-effect waves-dark' href=TotalTrade_Turnover.py target=mw><i class='mdi mdi-bullseye'></i><span class='hide-menu'>Total Traded Quantity VS Turnover(in Lakhs)</span></a></li>")
print("<li><a class='has-arrow waves-effect waves-dark' href=CloseP_TotalTrade_Turnover.py target=mw><i class='mdi mdi-bullseye'></i><span class='hide-menu'>Close Price And Total Traded Quantity VS Turnover(in Lakhs)</span></a></li>")
print("<li><a class='has-arrow waves-effect waves-dark' href=links.py target=mw><i class='mdi mdi-bullseye'></i><span class='hide-menu'>Prediction Of Data On Year Basis</span></a></li>")
print("<li><a class='has-arrow waves-effect waves-dark' href=mlinks.py target=mw><i class='mdi mdi-bullseye'></i><span class='hide-menu'>Prediction Of Data On Month Basis</span></a></li>")
print("<li><a class='has-arrow waves-effect waves-dark' href=HomeGraphs.py target=mw><i class='mdi mdi-bullseye'></i><span class='hide-menu'>Graphs</span></a></li>")

print("</ul>")
print("                </nav>")
print("            </div>")
print("        </aside>")
print("        <div class='page-wrapper'>")
print("            <div class='container-fluid'>")
print("                <div class='row'>")
print("                    <div class='col-12'>")
print("                        <div class='card'>")
print("                            <div class='card-body'>")
print("<iframe style='width:100%; height:800px;' frameborder=0 name=mw></iframe>")
print("                            </div>")
print("                        </div>")
print("                    </div>")
print("                </div>")
print("            </div>")
print("            <footer class='footer'>")
print("                © 2017 Admin Press Admin by themedesigner.in")
print("            </footer>")
print("        </div>")
print("    </div>")
print("    <script src='admin/assets/plugins/jquery/jquery.min.js'></script>")
print("    <script src='admin/assets/plugins/bootstrap/js/popper.min.js'></script>")
print("    <script src='admin/assets/plugins/bootstrap/js/bootstrap.min.js'></script>")
print("    <script src='admin/main/js/jquery.slimscroll.js'></script>")
print("    <script src='admin/main/js/waves.js'></script>")
print("    <script src='admin/main/js/sidebarmenu.js'></script>")
print("    <script src='admin/assets/plugins/sticky-kit-master/dist/sticky-kit.min.js'></script>")
print("    <script src='admin/assets/plugins/sparkline/jquery.sparkline.min.js'></script>")
print("    <script src='admin/main/js/custom.min.js'></script>")
print("    <script src='admin/assets/plugins/styleswitcher/jQuery.style.switcher.js'></script>")
print("</body>")
print("</html>")









