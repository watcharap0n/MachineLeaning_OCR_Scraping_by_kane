<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8"/>
    <title>login</title>
    <meta http-equiv="X-UA-Compatible" content="IE=edge"/>
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no"/>
    <link rel="icon" href="/static/images/4100.jpg" type="image/png" sizes="16x16">
    <!--    <link rel="stylesheet" href="css/custom.css">-->
    <meta name="description" content=""/>
    <meta name="author" content=""/>
    <!-- Custom fonts for this template-->
    <link href="https://fonts.googleapis.com/css?family=Roboto:100,300,400,500,700,900" rel="stylesheet">
    <link href="https://cdn.jsdelivr.net/npm/@mdi/font@4.x/css/materialdesignicons.min.css" rel="stylesheet">
    <link href="https://cdn.jsdelivr.net/npm/vuetify@2.x/dist/vuetify.min.css" rel="stylesheet">
    <link href="{{ url_for('static',filename='vendor/fontawesome-free/css/all.min.css') }}"
          rel="stylesheet"
          type="text/css"/>

    <link
            href="https://fonts.googleapis.com/css?family=Nunito:200,200i,300,300i,400,400i,600,600i,700,700i,800,800i,900,900i"
            rel="stylesheet"
    />
    <link
            rel="stylesheet"
            href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css"
    />
    <link
            rel="stylesheet"
            href="https://cdn.datatables.net/1.10.22/css/jquery.dataTables.min.css"
    />

    <!-- Custom styles for this template-->

    <link
            href="{{ url_for('static',filename='/css/sb-admin-2.min.css') }}"
            rel="stylesheet"
    />


    <!-- Bootstrap core JavaScript-->
    <script src="{{ url_for('static',filename='vendor/jquery/jquery.min.js') }}"></script>
    <script src="{{ url_for('static',filename='vendor/bootstrap/js/bootstrap.bundle.min.js') }}"></script>
    <script src="{{ url_for('static',filename='vendor/chart.js/Chart.min.js') }}"></script>
    <script src="{{ url_for('static',filename='js/qs.js/') }}"></script>

    <!-- Core plugin JavaScript-->

    <script src="{{ url_for('static',filename='vendor/jquery-easing/jquery.easing.min.js') }}"></script>

    <!-- Custom scripts for all pages-->
    <script src="{{ url_for('static',filename='js/sb-admin-2.min.js') }}"></script>
    <script src="https://cdn.jsdelivr.net/npm/vue@2.6.10/dist/vue.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
    <script src="http://cdn.datatables.net/1.10.21/js/jquery.dataTables.min.js"></script>
    <script src="https://static.line-scdn.net/liff/edge/versions/2.3.0/sdk.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/2.7.1/Chart.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/vue@2.x/dist/vue.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/vuetify@2.x/dist/vuetify.js"></script>
    <script src="https://unpkg.com/vue-chartjs/dist/vue-chartjs.min.js"></script>
    <link href="https://cdn.jsdelivr.net/npm/@mdi/font@5.x/css/materialdesignicons.min.css" rel="stylesheet">
    <script src="https://cdnjs.cloudflare.com/ajax/libs/axios/0.21.0/axios.min.js"
            integrity="sha512-DZqqY3PiOvTP9HkjIWgjO6ouCbq+dxqWoJZ/Q+zPYNHmlnI2dQnbJ5bxAHpAMw+LXRm4D72EIRXzvcHQtE8/VQ=="
            crossorigin="anonymous"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/axios/0.21.0/axios.js"
            integrity="sha512-bYkaBWaFtfPIMYt9+CX/4DWgfrjcHinjerNYxQmQx1VM76eUsPPKZa5zWV8KksVkBF/DaHSADCwil2J5Uq2ctA=="
            crossorigin="anonymous"></script>

    <!-- If you enabled Analytics in your project, add the Firebase SDK for Analytics -->
    <!-- <script src="https://www.gstatic.com/firebasejs/7.18.0/firebase-analytics.js"></script> -->

    <!-- Add Firebase products that you want to use -->
    <script src="https://cdn.jsdelivr.net/npm/sweetalert2@9"></script>
</head>

<body id="page-top">

<!-- Page Wrapper -->
<div >

    <!-- End of Sidebar -->

    <!-- Content Wrapper -->
    <div id="content-wrapper" class="d-flex flex-column">
        <!-- Main Content -->
        <div id="content">
            {% block content %}
            {% endblock %}
        </div>

    </div>
    <!-- End of Content Wrapper -->
</div>




</body>

</html>
